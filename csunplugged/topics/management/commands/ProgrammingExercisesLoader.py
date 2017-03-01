import yaml
import os
from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.models import LearningOutcome

class ProgrammingExercisesLoader(BaseLoader):

    def __init__(self, programming_exercises_structure, topic):
        super().__init__()
        self.programming_exercises_structure = programming_exercises_structure
        self.topic = topic

    def load(self):
        structure = yaml.load(open(os.path.join(self.BASE_PATH, self.programming_exercises_structure), encoding='UTF-8').read())

        for programming_exercise_data in structure:
            programming_exercise_content = BaseLoader.convert_md_file(programming_exercise_data['md-file'])

            programming_exercise = self.topic.topic_programming_exercises.create(
                slug=programming_exercise_data['slug'],
                name=programming_exercise_content.title,
                exercise_number=programming_exercise_data['exercise-number'],
                content=programming_exercise_content.html_string,
                scratch_hints=BaseLoader.convert_md_file(programming_exercise_data['scratch']['hints']).html_string,
                scratch_solution=BaseLoader.convert_md_file(programming_exercise_data['scratch']['solution']).html_string,
                python_hints=BaseLoader.convert_md_file(programming_exercise_data['python']['hints']).html_string,
                python_solution=BaseLoader.convert_md_file(programming_exercise_data['python']['solution']).html_string,
            )
            programming_exercise.save()

            for learning_outcome_slug in programming_exercise_data['learning-outcomes']:
                learning_outcome = LearningOutcome.objects.get(
                    slug=learning_outcome_slug
                )
                programming_exercise.learning_outcomes.add(learning_outcome)
            BaseLoader.load_log.append(('Added Programming Exercise: {}'.format(programming_exercise.name), 1))
