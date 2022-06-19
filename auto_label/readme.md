# Auto label

- Problem: OCR+NER =======> Anotator for this problem so hard and many time
- Target: Auto label position and text for this word in resume ==> decrease time for anotator

## 1 . SET UP

#### Install labels studio

```
docker pull heartexlabs/label-studio:latest
docker run -it -p 8080:8080 -v `pwd`/mydata:/label-studio/data heartexlabs/label-studio:latest
```

#### Step by Step

- Step 1: Create project in labels studio with OCR project
- Step 2: Upload all image to project and export json file (ex: init.json) and delete all tasks image in this project.
- Step 3: In the local database, you can file path for store all image above (ex: /mydata/media/upload/3/)
- Step 4: Run script

  ```python
   python3 auto_label/main.py \
      --path_in init.json \
      --path_out auto_label.json \
      --path_datasource /mydata/media/upload/3


  ```
- Step 5: import new file json (ex: auto_label.json)
- Step 6: Edit box and text and add tag
