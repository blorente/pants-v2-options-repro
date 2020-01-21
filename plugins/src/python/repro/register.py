from pants.goal.task_registrar import TaskRegistrar as task
from pants.task.task import Task


def register_goals():
    class DeprecatedTask(Task):
        deprecated_options_scope = 'test.deprecated'
        deprecated_options_scope_removal_version = '1.9999.0'

        @classmethod
        def register_options(cls, register):
            super().register_options(register)
            register('--unicorns', help="Just to test that register() closes the parent scope")

    task(name='deprecated', action=DeprecatedTask).install()