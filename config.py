
TAG2IDX = {
    "ADDRESS": 0, 
    "AWARD_NAME": 1, 
    "CAREER": 2, 
    "CER_DATE": 3,
    "CER_NAME": 4,  
    "EDU_DEGREE": 5,  
    "EDU_END_DATE": 6,  
    "EDU_START_DATE": 7,  
    "EDU_UNIVERSITY": 8,  
    "EMAIL": 9,  
    "EX_COMPANY": 10,  
    "EX_DESCRIPTION": 11,  
    "EX_END_DATE": 12,  
    "EX_LOCATION": 13,  
    "EX_POSITISION": 14,  
    "EX_START_DATE": 15,  
    "LANGUAGE": 16,  
    "NAME": 17,  
    "OTHER": 18,  
    "PHONE": 19,  
    "PROJECT_DESCRIPTION": 20,  
    "PROJECT_END_TIME": 21,  
    "PROJECT_NAME": 22,  
    "PROJECT_START_TIME": 23,  
    "SKILL": 24,  
    "SUMARIZE": 25,  
    "URL": 26
}

IDX2TAG = {v:k for k,v in TAG2IDX.items()}

TAG2COLOR = {
    "ADDRESS":"#0000FF",
    "AWARD_NAME":"#8A2BE2",
    "CAREER":"#A52A2A",
    "CER_DATE":"#7FFF00",
    "CER_NAME":"#6495ED",
    "EDU_DEGREE":"#DC143C",
    "EDU_END_DATE":"#FF7F50",
    "EDU_START_DATE":"#00008B",
    "EDU_UNIVERSITY":"#B8860B",
    "EMAIL":"#FF1493",
    "EX_COMPANY":"#228B22",
    "EX_DESCRIPTION":"#B22222",
    "EX_END_DATE":"#DAA520",
    "EX_LOCATION":"#CD5C5C",
    "EX_POSITISION":"#ADFF2F",
    "EX_START_DATE":"#4B0082",
    "LANGUAGE":"#90EE90",
    "NAME":"#FFA07A",
    "OTHER":"#FF4500",
    "PHONE":"#FFA500",
    "PROJECT_DESCRIPTION":"#DDA0DD",
    "PROJECT_END_TIME":"#4169E1",
    "PROJECT_NAME":"#2E8B57",
    "PROJECT_START_TIME":"#6A5ACD",
    "SKILL":"#EE82EE",
    "SUMARIZE":"#9ACD32",
    "URL":"#4682B4"
 }

MODEL_PATH = 'bestmodel.pt'
PRETRAIN_MODEL = 'pretrain/model'
PRETRAIN_PROCESSOR = 'pretrain/processor'