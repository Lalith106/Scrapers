from pathlib import Path
from datetime import datetime
import zipfile
root_dir=Path("files")

# file_paths = root_dir.glob("**/*")
# for path in file_paths:
#     if(path.is_file()):
#         print(path)
#         parent_folder = path.parts
#         p1_folder = parent_folder[-2]
#         p2_folder = parent_folder[-3]
#         new_filename = p1_folder+"-"+p2_folder+"-"+path.name
#         print(new_filename)
#         new_filepath = path.with_name(new_filename)
#         path.rename(new_filepath)

root_dir2 = Path("files2")
file_paths = root_dir2.glob("*.csv")
print(file_paths)
# for path in file_paths:
#     if(path.is_file()):
#         new_filepath = path.with_suffix(".csv")
#         path.rename(new_filepath)
        # curr_time = path.stat().st_ctime
        # created_date = datetime.fromtimestamp(curr_time)
        # formated_date = created_date.strftime("%Y-%m-%d_%H-%M-%S")
        # new_filename = formated_date+"-"+path.name
        # new_filepath = path.with_name(new_filename)
        # path.rename(new_filepath)

for i in range(10,16):
    file_name = str(i)+".txt"
    file_path = root_dir2 / Path(file_name)
    file_path.touch()
# for path in file_paths:
#     print(path)
#     if(path.is_file()):
#         path.unlink()
root_dir = Path("files2")
archive_path = root_dir / Path("archive2.zip")
file_paths = root_dir.rglob("*.txt")
with zipfile.ZipFile(archive_path,'w')as zf:
    for path in file_paths:
        zf.write(path)
        #path.unlink()

dir1 = Path("files2")
file_paths = dir1.glob("*.zip")
for path in file_paths:
    with zipfile.ZipFile(path,'r') as fl:
        dir2= dir1 / path.stem
        fl.extractall(dir2)
root = Path(".")
file_paths = root.rglob("**/*")
for path in file_paths:
    if("14" in path.name):
        print(path.absolute())



    




