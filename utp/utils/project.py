import os


class Project:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程目录
    projects_path = os.path.join(base_path, 'projects')  # 项目目录
    child_dirs = ['cases', 'data', 'report', 'public']

    def __init__(self, project_name):
        self.project_name = project_name
        self.project_path = os.path.join(self.projects_path, project_name)  # 要创建的项目目录

    def create_project(self):
        '''校验项目是否存在，不存在的话，创建'''
        if os.path.exists(self.project_path):
            raise Exception("项目已经存在！")
        else:
            os.mkdir(self.project_path)

    def create_init_py(self,path):
        '''
        创建__init__.py文件
        :param path: 路径
        :return:
        '''
        py_file_path = os.path.join(path, '__init__.py')
        self.write_content(py_file_path,'')#打开一个空文件

    def create_dir(self, ):
        '''创建项目下面的子目录'''
        for dir in self.child_dirs:
            dir_path = os.path.join(self.project_path, dir)
            os.mkdir(dir_path)
            if dir=='cases':#如果是cases文件夹的话，创建__init__.py
                #cases是个package查找用例的时候才会找到那个目录下所有子目录里面的测试用例
                self.create_init_py(dir_path)

    def create_run_py(self):
        '''生成run.py'''
        run_template_path = os.path.join(self.base_path, 'config', 'run_template')
        content = self.get_template_content(run_template_path).format(project_name=self.project_name)
        run_file_path = os.path.join(self.project_path, 'run.py')
        self.write_content(run_file_path, content)

    def create_const_py(self):
        '''生成const.py'''
        run_template_path = os.path.join(self.base_path, 'config', 'const_template')
        content = self.get_template_content(run_template_path)
        run_file_path = os.path.join(self.project_path, 'public', 'const.py')
        self.write_content(run_file_path, content)

    def main(self):
        '''创建项目'''
        self.create_project()  # 创建项目
        self.create_dir()  # 创建项目下面的文件夹
        self.create_run_py()  # 创建run.py
        self.create_const_py()  # 创建const.py

    @staticmethod
    def get_template_content(file_name):
        '''读取文件内容'''
        with open(file_name, encoding='utf-8') as fr:
            return fr.read()

    @staticmethod
    def write_content(file, content):
        '''写入文件'''
        with open(file, 'w', encoding='utf-8') as fw:
            fw.write(content)
