
from thothflow import Task


class TestTask:

    def test_create_task(self):

        class MyTask(Task):
            def run(self, scroll):
                scroll['value'] = scroll.get('value', 0) + 1
                return scroll

        task = MyTask()
        scroll = {}
        result = task.run(scroll)
        assert result['value'] == 1
