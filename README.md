# Meme Server
Veebirakendus, mis näitab igapäev uut IT meme et, oleks midagi, lähtudes Eesti kellaajast.

## Kirjeldus
- Mis see teeb?  
  See veebi rakendus näitab iga päev uut IT meemi, automaatselt vahetades pilti öösel kell 00:00 Eesti aja järgi. Lisaks kuvab rakendus ka taimeri mis uuendab end iga sekund, mis näitab, millal järgmine meem uuendatakse.

- Mis probleem lahendab?  
  Annab kasutajale midagi mida igapäev oodata :) ning annab visuaalset infot järgmise vahetuse aja kohta.

## Tööriistad
### 1. Git
Miks: Kontrollib versioone ja võimaldab koodi turvaliselt hallata.  
Kuidas integreerib: Kõik koodimuudatused salvestatakse gitiga ja saadetakse GitHubi.

### 2. GitHub Actions
Miks: CI / CD tööriist, mis tagab, et iga push värskendab pipelinei ja ehitab projekti automaatselt.  
Kuidas integreerib: Action fail .github/workflows/deploy.yml ehitab Docker image'i ja saab automaatselt deploy'ida või testida projekti.

### 3. Docker
Miks: Pakendab rakenduse koos kõikide sõltuvustega ühte konteinerisse, et seda saaks igal masinal jooksutada samamoodi.  
Kuidas integreerib: Dockerfile loob konteineri, mis sisaldab Flask serverit, pilte ja kõiki Python teeke.

### 4. Ansible
Miks: Automatiseerib serverisse deploy protsessi, sealhulgas Docker image ehitamise ja käivitamise.  
Kuidas integreerib: deploy.yml playbook tagab, et serveris oleks Docker installitud ja meme-server konteiner jooksuks õigesti.

### Tehisintellekti kasutasin peamiselt et anda sellele natuke visuaalsemat ilu ja debuggida koodi.

## Käivitamine

```bash
git clone https://github.com/MathMoell/meme-server.git
cd meme-server

# Ehita Docker image
docker build -t meme-server .

# Käivita konteiner
docker run -d -p 8080:8080 -v $(pwd)/memes:/app/memes --name meme-server meme-server
