### Are you eager to **dive into the world of algorithm creation** for the 5controls platform but feeling unsure where to start? 
Look no further! We are delighted to present to you our comprehensive repository, designed to **guide you** through the process of building your very own **protective jacket detection algorithm** and seamlessly **connecting it to the 5controls** platform.

### In this guide we will cover:

- Step 1: **Data Acquisition and Preparation**
  
- Step 2: **Algorithm Development**

- Step 3: **Testing and Evaluation**

- Step 4: **Integration with 5controls Platform**
  
During these steps you'll discover how to **build, test and seamlessly connect** your protective jacket detection algorithm to the 5controls platform, enabling it to **generate violation reports** and **contribute to a safer working environment**. 

With our repository as your guide, you'll gain the knowledge and skills needed to **create** a powerful protective jacket detection algorithm **within a matter of a couple of days**. 

### Follow the step-by-step instructions, study the commits history for valuable insights, and witness your algorithm come to life.

![b7f26b31-9eec-498a-b53c-08fc8724239c](https://github.com/5sControl/my-first-5s-algorithm/assets/131950264/b70dddee-f575-4b39-bad3-f6138095ff14)

# Getting started 

### 1. Build your project with commits history.
1) Write your algorthm;
2) Add your model and set some settings for the model. Specifically configure the parameters that we will accept from the model, for example:
<img width="960" alt="image" src="https://github.com/5sControl/my-first-5s-algorithm/assets/105813294/42d238ce-ea78-4a13-857c-e438c3789262">

3) Let's add a class in order to receive an image from the server;
4) The most important step: how to send the report. Everything is in this format:
   <img width="599" alt="image" src="https://github.com/5sControl/my-first-5s-algorithm/assets/105813294/d98d0063-b0cb-4be8-a313-b25cc9c1d731">

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

### 6. If all the steps are completed successfully, you will see your algorithm on the 5s platform!  

- You have to download models:
**Models**: https://drive.google.com/drive/folders/10sprtEcwOSMJPmn-5y0xi5QwlsDswrMx?usp=sharing
you have to download models 
