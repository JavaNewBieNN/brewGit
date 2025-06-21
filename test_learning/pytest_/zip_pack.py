import zipfile
import os

def zip_report_folder(folder_path='report', zip_name='report.zip'):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, folder_path)
                zipf.write(abs_path, arcname=os.path.join('report', rel_path))



"""
zipfile.ZipFile(...): 创建一个 zip 文件对象
'w': 写入模式（还有 'a' 追加模式）
zipfile.ZIP_DEFLATED: 使用压缩
os.walk(folder_path): 遍历整个目录树
abs_path: 文件的绝对路径
rel_path: 文件相对于 folder_path 的路径，这样 zip 里的结构就不会带上完整路径
arcname=...: 决定写进 zip 的路径结构（控制目录结构）
"""