import os
import shutil

def create_folder(path:str, folder:str):

    for f in os.listdir(path):
        folder_path = os.path.join(path, f)
        
        if os.path.isdir(folder_path) and not f.startswith("logs_"):
            print(f"Removing folder: {f}") 
            shutil.rmtree(folder_path)

    
    
    loggerFiles = f"{path}/{folder}"
    os.makedirs(loggerFiles)

def create_file(path:str, filesNumber:int):
    folder_list = []
    destination = []
    for f in os.listdir(path):
        if f.startswith("logs_"):
            folder_list.append(f)
        else:
            destination.append(f)
        
    destinationPath = f"{path}/{destination[0]}"
    if len(folder_list) != 0:
        for f in folder_list:
            files = os.listdir(f"{path}/{f}")
            for file in files[-filesNumber:]:
                shutil.copyfile(f"{path}/{f}/{file}", f"{destinationPath}/{file}")            
    else:
        print("No folders found")

    shutil.make_archive(f'{path}/zip/{destination[0]}', 'zip', destinationPath)


def create_zip(path:str, folder:str, filesNumber:int):
    create_folder(path, folder)
    create_file(path, filesNumber)
        
#__________________________________________________________

#Todays date, that can be used to name the folder

today = '2025-01-14'
#Add folder name
folder = f'{today}-logs'

# Create zip takes the path, the folder name and the number of files to be Ziped (path:str, folder:str, filesNumber:int)
create_zip('logger_files', folder, 2)