"""This is an email validation function that accepts an email as an argument
and returns a string indicating the validity of the email. The function is
divided into three blocks according to the format of the email to validate
'someone@example.top_domain' and the email is divided into three sections to validate
. Each blocks of the function validates each section and each section have it's own validator
of the email due to the given criteria and at the end the value of the validators
after undergoing tests from all blocks is used to determine the validity of the
email.
"""

def email_validate(email):
    try:
    #check if the email contains dot or @
        if '@' not in email or '.' not in email:
            return 'Invalid Email'
        else:
            validator1 = False
            validator2 = False
            validator3 = False
            at_index = email.find('@')
            dot_index = email.find('.')
            someone = email[0:at_index]
            sp_chars = ['!','@','#','$','%','^','&']
            example = email[at_index+1:dot_index]
            top_domain = email[dot_index+1:]
            #validate the someone part of the email
            for char in someone:
                if char.isupper() or char.isalnum()==False:
                    if char in sp_chars:
                        validator1 = True
                    else:
                        validator1 = False
                        break
                else:
                    validator1 = True

            #validate the example part of the email
            for char in example:
                if char.isupper() or char.isalnum()==False:
                    if char != '-':
                        validator2 = False
                        break
                    else:
                        validator2 = True
                else:
                    validator2 = True

            #Top domain validator block
            if '.' in top_domain:
                top_domain_list = top_domain.split('.')
                for char in top_domain_list:
                    if char.isalpha()==False:
                        validator3 = False
                        break
                    elif len(char)<2:
                        validator3 = False
                        break
                    else:
                        validator3 = True
            else:
                if len(top_domain)<2 or top_domain.isalpha()==False:
                    validator3 = False
                else:
                    validator3 = True

            #uses the validator bool to determine the validity of the email
            if validator1 == False or validator2 == False or validator3 == False:
                return 'Invalid email'
            else:
                return 'Valid email'
    except:
        return 'Invalid argument passed to the email validator function'

print(email_validate('oemmaniel200@yahoo.com'))
print(email_validate('emanueloluwatobi2000@gmail.com'))
print(email_validate('Arubiewe78@stu.ui.edu.ng'))
print(email_validate('oemmanuel681@stu.ui.edu.ng'))
print(email_validate('oemmanuel681@stu.ui.edu.ng'))
