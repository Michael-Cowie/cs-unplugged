"""Module for the custom Django loadtopics command."""

import os.path
from django.core.management.base import BaseCommand
from django.conf import settings
from utils.BaseLoader import BaseLoader
from utils.LoaderFactory import LoaderFactory
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class Command(BaseCommand):
    """Required command class for the custom Django loadtopics command."""

    help = "Converts Markdown files listed in structure file and stores"

    def add_arguments(self, parser):
        """Add optional parameter to loadtopics command."""
        parser.add_argument(
            "--lite-load",
            action="store_true",
            dest="lite_load",
            help="Perform lite load (only load key topics content)",
        )

    def handle(self, *args, **options):
        """Automatically called when the loadresources command is given.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        factory = LoaderFactory()
        lite_load = options.get("lite_load")

        # Get structure and content files
        base_loader = BaseLoader()
        base_path = settings.TOPICS_CONTENT_BASE_PATH

        structure_file_path = os.path.join(
            base_path,
            base_loader.structure_dir,
            "structure.yaml"
        )

        structure_file = base_loader.load_yaml_file(structure_file_path)

        if "curriculum-areas" in structure_file:
            curriculum_areas_structure_file_path = structure_file["curriculum-areas"]
            if curriculum_areas_structure_file_path is not None:
                curriculum_areas_path, structure_filename = os.path.split(curriculum_areas_structure_file_path)
                factory.create_curriculum_areas_loader(
                    base_path=base_path,
                    content_path=curriculum_areas_path,
                    structure_filename=structure_filename
                ).load()

        if "learning-outcomes" in structure_file:
            learning_outcomes_structure_file_path = structure_file["learning-outcomes"]
            if learning_outcomes_structure_file_path is not None:
                learning_outcomes_path, structure_filename = os.path.split(learning_outcomes_structure_file_path)
                factory.create_learning_outcomes_loader(
                    base_path=base_path,
                    content_path=learning_outcomes_path,
                    structure_filename=structure_filename
                ).load()

        if "programming-challenges-structure" in structure_file:
            programming_challenges_structure_file_path = structure_file["programming-challenges-structure"]
            if programming_challenges_structure_file_path is not None:
                programming_challenges_path, structure_filename = os.path.split(
                    programming_challenges_structure_file_path
                )
                factory.create_programming_challenges_structure_loader(
                    base_path=base_path,
                    content_path=programming_challenges_path,
                    structure_filename=structure_filename
                ).load()

        if "classroom-resources" in structure_file:
            classroom_resources_structure_file_path = structure_file["classroom-resources"]
            if classroom_resources_structure_file_path is not None:
                classroom_resources_path, structure_filename = os.path.split(
                    classroom_resources_structure_file_path
                )
                factory.create_classroom_resources_loader(
                    base_path=base_path,
                    content_path=classroom_resources_path,
                    structure_filename=structure_filename
                ).load()

        if "glossary-folder" in structure_file:
            glossary_folder_path = structure_file["glossary-folder"]
            if glossary_folder_path is not None:
                factory.create_glossary_terms_loader(
                    base_path=base_path,
                    content_path=glossary_folder_path,
                ).load()

        age_groups_structure_file_path = structure_file.get("age-groups", None)
        if age_groups_structure_file_path is None:
            raise MissingRequiredFieldError(
                structure_file_path,
                ["age-groups"],
                "Application Structure"
            )
        else:
            age_groups_path, structure_filename = os.path.split(age_groups_structure_file_path)
            factory.create_age_groups_loader(
                content_path=age_groups_path,
                base_path=base_path,
                structure_filename=structure_filename
            ).load()

        if structure_file.get("topics", None) is None or not isinstance(structure_file["topics"], list):
            raise MissingRequiredFieldError(
                structure_file_path,
                ["topics"],
                "Application Structure"
            )
        else:
            for topic in structure_file["topics"]:
                topic_path = topic
                topic_structure_file = "{}.yaml".format(topic)
                factory.create_topic_loader(
                    base_path=base_path,
                    content_path=topic_path,
                    structure_filename=topic_structure_file,
                    lite_loader=lite_load,
                ).load()
