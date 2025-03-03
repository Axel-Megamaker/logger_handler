import os
import shutil
import logging
from datetime import datetime

#___________LOGGER_____________________________________________________________________________________________________________________________________________
logger_folder = os.path.join('logger_files', 'logs_LoggerHandler')
file_ini = 'LH'
today = datetime.now().strftime("%Y-%m-%d")
logging.basicConfig(filename=os.path.join(logger_folder, f'{file_ini}_{today}'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#___________________________________________________________________________________________________________________________________________________________

#============Functions==================================
def create_zip(path:str, folder:str, filesNumber:int):
    #==================Create folder======================================================================
    for f in os.listdir(path):
        folder_path = os.path.join(path, f)

        if os.path.isdir(folder_path) and not f.startswith("logs_"):
            logger.info(f'Removed folder: {f}') 
            shutil.rmtree(folder_path)

    loggerFiles = os.path.join(path,folder)
    os.makedirs(loggerFiles)
    logger.info(f'Added folder: {folder}') 
    
    #==================Create file==============================================================================
    folder_list = []
    destination = []
    for f in os.listdir(path):
        if f.startswith("logs_"):
            folder_list.append(f)
            logger.info(f'Added: {f} to list of log folders') 
        else:
            destination = f
            logger.info(f'File to be zipped: {destination}') 
        
    destinationPath = os.path.join(path,destination)
    if len(folder_list) != 0:
        logger.info(f'Log folders: {len(folder_list)}') 
        for folder in folder_list:
            files = os.listdir(os.path.join(path, folder))
            for file in files[-filesNumber:]:
                shutil.copyfile(os.path.join(path, folder, file), os.path.join(destinationPath, file))
                logger.info(f'Copying: {file} TO FOLDER {destinationPath}')             
    else:
        logger.info(f'No folders found') 

    logger.info(f'Created zipfile: {destination}.zip IN FOLDER {path}\zip')
    shutil.make_archive(os.path.join(path, "zip", destination), "zip", destinationPath)
    #=======================================================================================================

def remove_files(path:str, numberOfDays:int):
    folder_list = []
    file_list = []
    for f in os.listdir(path):
        if f.startswith("logs_"):
            folder_list.append(f)

    if len(folder_list) != 0:
        for folder in folder_list:
            files = os.listdir(os.path.join(path, folder))
            for file in files:
                file_list.append(file)
            if len(file_list) >= numberOfDays:
                print(f'{folder} : ({len(file_list)} file[s])')

                n = len(file_list) - numberOfDays
                if n >= 0:
                    print(file_list[:n])
                    for f in file_list[:n]:#
                        os.remove(os.path.join(path, folder, f))
            else:
                print(f'{folder} : {len(file_list)} file[s]')
            file_list.clear()

#===================Main==================================
today = datetime.now().strftime("%Y-%m-%d")

path = 'logger_files'
folder = f'{today}-logs'
filesNumber = 3

create_zip(path, folder, filesNumber)