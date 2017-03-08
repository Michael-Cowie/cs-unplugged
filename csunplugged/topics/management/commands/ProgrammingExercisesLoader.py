from utils.BaseLoader import BaseLoader
from topics.models import (
    LearningOutcome,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
    ProgrammingExerciseLanguageImplementation,
)


class ProgrammingExercisesLoader(BaseLoader):
    """Loader for programming exercises"""

    def __init__(self, load_log, structure_file, topic):
        """Initiates the loader for programming exercises

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(load_log)
        self.structure_file = structure_file
        self.topic = topic

    def load(self):
        """load the content for programming exercises"""
        if self.structure_file:
            structure = self.load_yaml_file(self.BASE_PATH.format(self.structure_file))

            # For each programming exercise
            for exercise in structure:
                content = self.convert_md_file(self.BASE_PATH.format(exercise['md-file']))

                programming_exercise = self.topic.topic_programming_exercises.create(
                    slug=exercise['slug'],
                    name=content.title,
                    exercise_number=exercise['exercise-number'],
                    content=content.html_string,
                    difficulty=ProgrammingExerciseDifficulty.objects.get(
                        level=exercise['difficulty-level']
                    )
                )
                programming_exercise.save()

                language_solutions = exercise['programming-languages']
                for language in language_solutions:
                    # This gets the language for the solution, if not found it should throw an error!
                    language_object = ProgrammingExerciseLanguage.objects.get(
                        slug=language
                    )
                    hint_path = self.BASE_PATH.format(language_solutions[language]['hints'])
                    hint_content = self.convert_md_file(hint_path).html_string

                    solution_path = self.BASE_PATH.format(language_solutions[language]['solution'])
                    solution_content = self.convert_md_file(solution_path).html_string

                    solution = ProgrammingExerciseLanguageImplementation.objects.create(
                        hints=hint_content,
                        solution=solution_content,
                        language=language_object,
                        exercise=programming_exercise,
                        topic=self.topic
                    )
                    solution.save()

                for learning_outcome_slug in exercise['learning-outcomes']:
                    learning_outcome = LearningOutcome.objects.get(
                        slug=learning_outcome_slug
                    )
                    programming_exercise.learning_outcomes.add(learning_outcome)

                LOG_TEMPLATE = 'Added Programming Exercise: {}'
                self.log(LOG_TEMPLATE.format(programming_exercise.name), 1)
