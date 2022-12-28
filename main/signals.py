from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Visitor,Member
import json
import requests
import os


apiKey = 'GUQmiCmqNKLJd9EuQvPV3796gRFBaLJQGzcYbzoYjaIwj'
endPoint = 'https://api.mnotify.com/api/sms/quick'

url = endPoint + '?key=' + apiKey



@receiver(post_save, sender=Member)
def sms_congrate_to_new_member(sender,instance,created,**kwargs):
	if created:

		full_name = instance.full_name
		mobile = instance.mobile
		serve_in = instance.wheer_to_serve

		msg = f'Hello {full_name}, Congratulations on your decision to be part of this great Family and Commission. '
		msg = msg + f'The head of {serve_in} Department will get in touch with you soon.'

		if mobile != "":
			data = {
		  'recipient[]': [mobile],
		  'sender': 'EICC',
		  'message': msg,
		  'is_schedule': False,
		  'schedule_date': ''
			}

		# try:

			response = requests.post(url, data)
			data = response.json()

		# except Exception as e:
			# raise "Unknown error has occured, please try again later!"
		# else:
		# 	pass
		# finally:
		# 	pass




@receiver(post_save, sender=Visitor)
def sms_msg_to_visitor(sender,instance,created,**kwargs):
	if created:

		full_name = instance.full_name
		mobile = instance.mobile
		wish_to = instance.wish_to_be_a_member

		msg = f"Hello {full_name}, Trust you were blessed by today's service. God bless you for coming!! "
		
		if wish_to == "yes":
			msg = msg + f"Our chief officer will get in touch with you soon"

		if wish_to == "just visiting" or wish_to == "still considering":
			msg = msg + f"We look forward to your next visit."

		if mobile != "":
			data = {
		  'recipient[]': [mobile],
		  'sender': 'EICC',
		  'message': msg,
		  'is_schedule': False,
		  'schedule_date': ''
			}
					

		# try:
			
			response = requests.post(url, data)
			data = response.json()

		# except Exception as e:
			# raise "An expected error occured, please try again!"
		# else:
		# 	pass
		# finally:
		# 	pass




	