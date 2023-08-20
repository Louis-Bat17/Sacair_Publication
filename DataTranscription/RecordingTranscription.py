import assemblyai as aai
import json
import os

def IterateFiles(FolderPath):  
    # Iterate over files in given path then send them for transcribing, if any exist
    if os.path.exists(FolderPath) and os.path.isdir(FolderPath):
        FileList = os.listdir(FolderPath)
        RecordingFiles = [file for file in FileList if os.path.isfile(os.path.join(FolderPath, file))]
        for FileName in RecordingFiles:
            FileTranscribe = ".\\" + FolderPath + "\\" + FileName
            TranscribeExport = TranscribeData(FileTranscribe)
    else:
        print(f"Folder '{FolderPath}' does not exist.")

def TranscribeData(FileName):
    # get key from directory
    with open('mykey.json') as f:
        data = json.load(f)
    aai.settings.api_key = data['api_key']
    transcriber = aai.Transcriber()
    # call api then upload recording
    transcript = transcriber.transcribe(FileName)
    TranscriptionText = transcript.text
    # export raw data
    ExportRaw(FileName ,TranscriptionText)

def ExportRaw(FileName, rawText):
    # Append the transcription text to a text file
    ExportData = "transcription_output.txt"
    # Only include Filename for export
    file_name = FileName.split('\\')[-1] # remove path
    FileName = file_name.replace('.mp4', '') # remove .mp4 in this case

    with open(ExportData, "a") as TranscribeFile:
        TranscribeFile.write("\n\n" + FileName + "\n" + rawText)

if __name__ == "__main__":
    BeginProcess = IterateFiles('VoiceRecordings')