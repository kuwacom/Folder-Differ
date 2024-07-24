import os
import shutil

def getAllFiles(rootDir):
    fileList = []
    for dirpath, _, filenames in os.walk(rootDir):
        for filename in filenames:
            filePath = os.path.relpath(os.path.join(dirpath, filename), rootDir)
            fileList.append(filePath)
    return fileList

def copyNewFiles(oldDir, newDir, outputDir):
    # 出力ディレクトリが存在しない場合作成
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)


    oldFiles = set(getAllFiles(oldDir))
    newFiles = set(getAllFiles(newDir))

    filesToCopy = newFiles - oldFiles

    for filePath in filesToCopy:
        oldFilePath = os.path.join(newDir, filePath)
        newFilePath = os.path.join(outputDir, filePath)

        newFileDir = os.path.dirname(newFilePath)
        os.makedirs(newFileDir, exist_ok=True)
        
        shutil.copy2(oldFilePath, newFilePath)
        print(f"Copied: {filePath}")

if __name__ == "__main__":
    oldDir = "../Sort-Binary/assets"
    newDir = "../Sort-Binary/assets-1.47.291161"
    outputDir = "./output"

    copyNewFiles(oldDir, newDir, outputDir)
