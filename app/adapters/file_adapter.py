from app.ports.file_port import FilePort

class FileAdapter(FilePort):
    def read_file(self, file_content):
        return file_content

    def write_file(self, content, file_name):
        # Esta función se implementaría si necesitamos escribir archivos
        pass
