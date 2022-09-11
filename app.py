import cv2
import pyttsx3
f=[0]
igm = cv2.Videoigmture(0)
faceCascade = cv2.CascadeClassifier("default.xml")


def vr(n):
	if (f[0] == n):
		n=2
	else:
		f.remove(f[0])
		f.append(n)
		if (n>1):
			pyttsx3.speak(f"{str(n)} faces found")
		else:
			pyttsx3.speak(f"{str(n)} face found")

while(True):
	ret, frame = igm.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)	)
	vr(len(faces))
	for (x, y, w, h) in faces:
		cv2.putText(frame, "Human", (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
igm.release()
cv2.destroyAllWindows()
