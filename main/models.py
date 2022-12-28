from django.db import models




class Member(models.Model):
	m_status = (
		("Single","Single"),
		("Married","Married"),
		("Separated","Separated")
		)

	wh_choice = (
		("Ushering","Ushering"),
		("Music","Music"),
		("Envagelism","Envagelism"),
		("Prayer","Prayer"),
		("Media","Media")
		)
	full_name = models.CharField(max_length=50)
	date_of_membership = models.DateField(auto_now_add=True)
	date_of_birth = models.DateField()
	mobile = models.CharField(max_length=10, blank=True)
	email = models.EmailField(max_length=255,blank=True,null=True)
	palce_of_resident = models.CharField(max_length=150)
	occupation = models.CharField(max_length=150)
	marital_status = models.CharField(max_length=10,choices=m_status)
	name_of_spouse = models.CharField(max_length=150, blank=True,null=True)
	number_of_children = models.CharField(max_length=2, blank=True, null=True)
	is_baptized = models.BooleanField("Have you been baptisez?",default=False)
	wheer_to_serve = models.CharField(max_length=20,choices=wh_choice)

	def __str__(self):
		return self.full_name




class Visitor(models.Model):
	wich_to_choices = (
		("yes","Yes"),
		("just visiting","Just Visiting"),
		("still considering","Still considering")
		)

	full_name = models.CharField(max_length=50)
	date_of_first_visit = models.DateField(auto_now_add=True)
	is_confessed_jesus = models.BooleanField("Confessed Jesus Christ?",default=False, 
		help_text="Have you Confessed Jesus Christ as your Lord and personl savior?")
	mobile = models.CharField(max_length=10, blank=True)
	palce_of_resident = models.CharField(max_length=150)
	invited_by = models.CharField(max_length=150)
	current_place_of_fellowship = models.CharField(max_length=255, blank=True)

	wish_to_be_a_member = models.CharField(max_length=30,choices=wich_to_choices)
	prayer_request = models.TextField(blank=True)

	def __str__(self):
		return self.full_name
