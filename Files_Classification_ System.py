import os, shutil

# NOTE: You can write every single extensions inside tuples 
dict_extensions = {
    'Audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'Video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'Document_extensions' : ('.doc', '.docx', '.odt', '.pdf', '.txt', '.xls', '.xlsx', '.ppt','.pptx','.html'),
    'Image_extensions' : ('.gif', '.png', '.jpg', '.psd', '.tiff', '.eps'),
}

folderpath = input('Enter Folder Path : ')

def file_finder(folder_path, file_extensions):
      files = []
      for file in os.listdir(folder_path):
          for extension in file_extensions:
              if file.endswith(extension):
                  files.append(file)
      return files
    #I can also use in one line. OR (Like given bellow)
    #return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]


for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    
    if os.path.exists(folder_path):
        print(str(folder_path+'Folders are already Exists!'))
    else:
        os.mkdir(folder_path)       
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
        
        
        
        
  
