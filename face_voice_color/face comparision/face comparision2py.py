'''import boto3

def compare_faces(sourceFile, targetFile):

    client=boto3.client('rekognition')
   
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')

    response=client.compare_faces(SimilarityThreshold=80,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()     
    return len(response['FaceMatches'])          

def main():
    source_file='source'
    target_file='target'
    face_matches=compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))

if __name__ == "__main__":
    main()
'''

import face_recognition 
known_image = face_recognition.load_image_file("face_detected.jpg") 
unknown_image = face_recognition.load_image_file("face_detected.jpg") 
 
biden_encoding = face_recognition.face_encodings(known_image)[0] 
unknown_encoding = face_recognition.face_encodings(unknown_image)[0] 
 
results = face_recognition.compare_faces([biden_encoding], unknown_encoding) 
