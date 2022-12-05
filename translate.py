from textblob import TextBlob
text = TextBlob("Semáforo.")
print(text.translate(from_lang='es', to='en'))
