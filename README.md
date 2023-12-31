### Are you eager to **dive into the world of algorithm creation** for the 5controls platform but feeling unsure where to start? 
Look no further! We are delighted to present to you our comprehensive repository, designed to **guide you** through the process of building your very own **protective jacket detection algorithm** and seamlessly **connecting it to the 5controls** platform.

### In this guide we will cover:

- Step 1: **Algorithm Development**

- Step 2: **Integration with 5controls Platform**
  
During these steps you'll discover how to **build, test and seamlessly connect** your protective jacket detection algorithm to the 5controls platform, enabling it to **generate violation reports** and **contribute to a safer working environment**. 

With our repository as your guide, you'll gain the knowledge and skills needed to **create** a powerful protective jacket detection algorithm **within a matter of a couple of days**. 

### Follow the step-by-step instructions, study the commits history for valuable insights, and witness your algorithm come to life.

![image](https://github.com/5sControl/my-first-5s-algorithm/assets/131950264/1ccf5ac5-9be7-415a-b725-3da69c39756b)


# Getting started 

### 1. Build your project with commits history.
1) [Write your algorthm](https://github.com/5sControl/my-first-5s-algorithm/commit/79ce48b425dd9733c82d024c451b582ae7453b9f);
2) Add your model and set some settings for the model. [Specifically configure the parameters that we will accept from the model](https://github.com/5sControl/my-first-5s-algorithm/commit/6b177c5d297ab0f1b4133de44ca78aae2e6635ce).
 
> You have to download [the models](https://drive.google.com/drive/folders/10sprtEcwOSMJPmn-5y0xi5QwlsDswrMx?usp=sharing)
<img width="500" alt="image" src="https://github.com/5sControl/my-first-5s-algorithm/assets/105813294/42d238ce-ea78-4a13-857c-e438c3789262">

3) Let's [add a class](https://github.com/5sControl/my-first-5s-algorithm/commit/ae6205f39a7fefadfc7845ee6b92e00e0d7ea4a9) in order to receive an image from the server:

<img width="500" alt="image" src="https://github.com/5sControl/my-first-5s-algorithm/assets/105813294/2bcb9aa3-3dba-439c-ad7a-f9ce44dfb511">

4) The most important step: [configuring report sending](https://github.com/5sControl/my-first-5s-algorithm/commit/ae6205f39a7fefadfc7845ee6b92e00e0d7ea4a9). Everything must be in the following format:


<img width="500" alt="image" src="https://github.com/5sControl/my-first-5s-algorithm/assets/105813294/d98d0063-b0cb-4be8-a313-b25cc9c1d731">
<br>
   
<img width="500" alt="image" src="https://github.com/5sControl/my-first-5s-algorithm/assets/105813294/00adec38-d8a0-4240-8c0e-a51b6ab89cc8">

### 2. Run/Test code
  ```python vest.py```

### 3. Build image for my-first-5s-algorithm algorithm
- For x86 users

    ```docker build -t 5scontrol/my-first-5s-algorithm:latest .```

- for AArch64 users 

    ```docker buildx build --platform linux/amd64 -t 5scontrol/my-first-5s-algorithm:latest .```

### 4. Push images

  ```docker push 5scontrol/my-first-5s-algorithm:latest```

### 5. Pulling images on the server

Go to 5controlS UI, Configuration tab.  Click on the Add algorithm button.

<img width='500' alt = 'image' src="https://github.com/5sControl/my-first-5s-algorithm/assets/105813294/53fee963-1e4a-4740-94c2-17edc82720e3">

Fill in the form, specifying the information about your algorithm and its docker image.

![image](https://github.com/5sControl/my-first-5s-algorithm/assets/131950264/7fb70a8f-2f9a-494a-acf1-a7e8e258188a)


### 6. If all the steps are completed successfully, you will see your algorithm on the 5s platform!  

# **License**
[AGPL-3.0](LICENSE)

> This algorithm uses third party libraries that are distributed under their own terms (see [LICENSE-3RD-PARTY.md](https://github.com/5sControl/my-first-5s-algorithm/blob/main/LICENSE-3RD-PARTY.md)).<br>

<br>
<div align="center">
  <a href="https://5controls.com/" style="text-decoration:none;">
    <img src="https://github.com/5sControl/Manufacturing-Automatization-Enterprise/blob/3bafa5805821a34e8b825df7cc78e00543fd7a58/assets/Property%201%3DVariant4.png" width="10%" alt="" /></a> 
  <img src="https://github.com/5sControl/5s-backend/assets/131950264/d48bcf5c-8aa6-42c4-a47d-5548ae23940d" width="3%" alt="" />
  <a href="https://github.com/5sControl" style="text-decoration:none;">
    <img src="https://github.com/5sControl/Manufacturing-Automatization-Enterprise/blob/3bafa5805821a34e8b825df7cc78e00543fd7a58/assets/github.png" width="4%" alt="" /></a>
  <img src="https://github.com/5sControl/5s-backend/assets/131950264/d48bcf5c-8aa6-42c4-a47d-5548ae23940d" width="3%" alt="" />
  <a href="https://www.youtube.com/@5scontrol" style="text-decoration:none;">
    <img src="https://github.com/5sControl/Manufacturing-Automatization-Enterprise/blob/ebf176c81fdb62d81b2555cb6228adc074f60be0/assets/youtube%20(1).png" width="5%" alt="" /></a>
</div>
