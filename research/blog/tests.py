from django.contrib.auth.models import User
from blog import models
from datetime import date
def populate():
    User.objects.all().delete()
    models.Profile.objects.all().delete()
    models.Project.objects.all().delete()
    models.ResearchArea.objects.all().delete()
    models.Post.objects.all().delete()
    models.Comment.objects.all().delete()

    #read file
    file_open =  open("research.txt", "r")
    file_read = file_open.read()

    # superuser
    user = User.objects.create_superuser(username='admin', password='1234')

    # profiles
    user1 = User.objects.create_user(username='jmwai', password='1234')
    profile1 = models.Profile.objects.create(user=user1, first_name="John", last_name="Mwai", headline="hello",
                                    info="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean m",
                                    linkedin="https://getbootstrap.com/docs/4.0/layout/grid/", github="https://getbootstrap.com/docs/4.0/layout/grid/",
                                    facebook="https://getbootstrap.com/docs/4.0/layout/grid/",instagram="https://getbootstrap.com/docs/4.0/layout/grid/",twitter="https://getbootstrap.com/docs/4.0/layout/grid/",
                                    picture="images/profile.jpg", resume="docs/John_Mwai_cv.pdf",
                                    skills='Python,HTML,CSS,JavaScript,Django')
      # research areas
    area1 = models.ResearchArea.objects.create(title='Web Dev', desription=file_read,image="images/webdev.jpg")
    area1.team.add(profile1)
    area1.save()

    area2 = models.ResearchArea.objects.create(title='Robotics', desription=file_read, image="images/robotics.jpg")
    area2.team.add(profile1)
    area2.save()

    area3 = models.ResearchArea.objects.create(title='Machine Learning', desription=file_read, image="images/ml.jpg")
    area3.team.add(profile1)
    area3.save()

    area4 = models.ResearchArea.objects.create(title='Computer Vision', desription=file_read,image="images/computervision.jpg")
    area4.team.add(profile1)
    area4.save()


    # projects
    project1 = models.Project.objects.create(title="Research Website", abstract=file_read,
                                             image="images/website.jpg", html_content="")
    project1.collaborators.add(profile1)
    project1.save()
    project2 = models.Project.objects.create(title="Robotic Operating System", abstract=file_read,
                                             image="images/robots.jpg", html_content="")
    project2.collaborators.add(profile1)
    project2.save()
    project3 = models.Project.objects.create(title="Solar Wings", abstract=file_read,
                                             image="images/drone.jpg")
    project3.collaborators.add(profile1)
    project3.save()

    project4 = models.Project.objects.create(title="Colorful Camels", abstract=file_read,
                                             image="images/colorful_ucLed13.jpeg")
    project4.collaborators.add(profile1)
    project4.save()

    project5 = models.Project.objects.create(title="Package Management", abstract=file_read,
                                             image="images/cyber.jpg")
    project5.collaborators.add(profile1)
    project5.save()

    project6 = models.Project.objects.create(title="Discovery Teaching", abstract=file_read,
                                             image="imagesdt.png")
    project6.collaborators.add(profile1)
    project6.save()

    project7 = models.Project.objects.create(title="Career Website", abstract=file_read,
                                             image="images/career.jpeg")
    project7.collaborators.add(profile1)
    project7.save()

    project8 = models.Project.objects.create(title="Mechanical Clock", abstract=file_read,image="images/mechanical.jpg")
    project8.collaborators.add(profile1)
    project8.save()


    post1 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project1, title= "Telling Your Story", html_content = file_read, image="images/cyber.jpg")
    post1.save()

    post2 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project2, title= "Industry Preparation", html_content = file_read, image="images/dt.jpg")
    post2.save()

    post3 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project3, title= "Power Of Knowledge", html_content = file_read, image="images/webdev.jpg")
    post3.save()

    post4 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project4, title= "The 4th Revolution", html_content = file_read, image="images/drone.jpg")
    post4.save()

    post5 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project5, title= "Package Automation", html_content = file_read, image="images/computervision.jpg")
    post5.save()

    post6 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project6, title= "Technology-Supported Learning", html_content = file_read, image="images/dt.jpg")
    post6.save()

    post7 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project7, title= "Simplicity", html_content = file_read, image="images/website.jpg")
    post7.save()

    post8 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project8, title= "Revolutionary Systems", html_content = file_read, image="images/robot.jpg")
    post8.save()

    post9 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project7, title= "Perdictive Analysis", html_content = file_read, image="images/robots.jpg")
    post9.save()

    post10 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project7, title= "Equality in College Environment", html_content = file_read, image="images/colorful_ucLed13.jpeg")
    post10.save()

    post11 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project1, title= "Mobile Robotics", html_content = file_read, image="images/robot.jpg")
    post11.save()

    post12 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project2, title= "Mathematical Modelling", html_content = file_read, image="images/webdev.jpg")
    post12.save()

    post13 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project3, title= "Sentiment Analysis", html_content = file_read, image="images/mechanical.jpg")
    post13.save()

    post14 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project4, title= "Power Of Time", html_content = file_read, image="images/ml.jpg")
    post14.save()

    post15 = models.Post.objects.create(author=profile1, creation_date=date.today(), project =project5, title= "Facial Recognition", html_content = file_read, image="images/robotics.jpg")
    post15.save()

populate()
