"# networksecurity" 
docker commands step-by-step:

1)docker buildx build -t phishingcontainer01.azurecr.io/networksecurityfastapi:latest .

2)docker login  phishingcontainer01.azurecr.io

3)docker push phishingcontainer01.azurecr.io/networksecurityfastapi:latest 