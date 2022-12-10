from flask import Flask, render_template, request

app = Flask(__name__)

def generate_about_my_type(my_type):
    if my_type == '1':
        return [
            "Type 1 individuals are rational, idealistic, and principled.",
            "They are perfectionists who strive for fairness and justice.",
            "They are organized and responsible, and value honesty and integrity.",
        ]
    elif my_type == '2':
        return [
            "Type 2 individuals are empathetic, warm, and caring.",
            "They are supportive and want to be of service to others.",
            "They are sensitive to the needs of others and are often good listeners.",
        ]
    elif my_type == '3':
        return [
            "Type 3 individuals are adaptable, ambitious, and driven.",
            "They are focused on achieving success and seek to be the best at what they do.",
            "They are image-conscious and want to be seen as successful and competent.",
        ]
    elif my_type == '4':
        return [
            "Type 4 individuals are sensitive, individualistic, and introspective.",
            "They are creative and artistic, and often have a unique and personal style.",
            "They are emotionally complex and can be both self-aware and self-absorbed.",
        ]
    elif my_type == '5':
        return [
            "Type 5 individuals are perceptive, cerebral, and investigative.",
            "They are knowledgeable and seek to understand the world around them.",
            "They are independent and self-sufficient, and value their privacy and personal space.",
        ]
    elif my_type == '6':
        return [
            "Type 6 individuals are loyal, committed, and hardworking.",
            "They are responsible and dutiful, and seek security and stability.",
            "They can be anxious and fearful, but also courageous and resilient.",
        ]
    elif my_type == '7':
        return [
            "Type 7 individuals are energetic, spontaneous, and optimistic.",
            "They are adventurous and enjoy trying new things and exploring new ideas.",
            "They can be scattered and restless, but also enthusiastic and fun-loving.",
        ]
    elif my_type == '8':
        return [
            "Type 8 individuals are assertive, strong-willed, and self-confident.",
            "They are powerful and decisive, and seek to be in control of their lives.",
            "They can be confrontational and intimidating, but also protective and supportive.",
        ]
    elif my_type == '9':
        return [
            "Type 9 individuals are easygoing, receptive, and good-natured.",
            "They are peaceful and accepting, and seek to maintain harmony in their relationships.",
            "They can be indecisive and avoidant, but also compassionate and empathetic.",
        ]

def generate_about_their_type(their_type):
    if their_type == '1':
        return [
            "Type 1 individuals are rational, idealistic, and principled.",
            "They are perfectionists who strive for fairness and justice.",
            "They are organized and responsible, and value honesty and integrity.",
        ]
    elif their_type == '2':
        return [
            "Type 2 individuals are empathetic, warm, and caring.",
            "They are supportive and want to be of service to others.",
            "They are sensitive to the needs of others and are often good listeners.",
        ]
    elif their_type == '3':
        return [
            "Type 3 individuals are adaptable, ambitious, and driven.",
            "They are focused on achieving success and seek to be the best at what they do.",
            "They are image-conscious and want to be seen as successful and competent.",
        ]
    elif their_type == '4':
        return [
            "Type 4 individuals are sensitive, individualistic, and introspective.",
            "They are creative and artistic, and often have a unique and personal style.",
            "They are emotionally complex and can be both self-aware and self-absorbed.",
        ]
    elif their_type == '5':
        return [
            "Type 5 individuals are perceptive, cerebral, and investigative.",
            "They are knowledgeable and seek to understand the world around them.",
            "They are independent and self-sufficient, and value their privacy and personal space.",
        ]
    elif their_type == '6':
        return [
            "Type 6 individuals are loyal, committed, and hardworking.",
            "They are responsible and dutiful, and seek security and stability.",
            "They can be anxious and fearful, but also courageous and resilient.",
        ]
    elif their_type == '7':
        return [
            "Type 7 individuals are energetic, spontaneous, and optimistic.",
            "They are adventurous and enjoy trying new things and exploring new ideas.",
            "They can be scattered and restless, but also enthusiastic and fun-loving.",
        ]
    elif their_type == '8':
        return [
            "Type 8 individuals are assertive, strong-willed, and self-confident.",
            "They are powerful and decisive, and seek to be in control of their lives.",
            "They can be confrontational and intimidating, but also protective and supportive.",
        ]
    elif their_type == '9':
        return [
            "Type 9 individuals are easygoing, receptive, and good-natured.",
            "They are peaceful and accepting, and seek to maintain harmony in their relationships.",
            "They can be indecisive and avoidant, but also compassionate and empathetic.",
        ]

def generate_communication(my_type, their_type):
    if my_type == '1' and their_type == '2':
        return "Type 1 individuals and Type 2 individuals can have good communication, as they both value being fair and honest. Type 1s can help Type 2s stay focused on their goals, and Type 2s can help Type 1s be more empathetic and considerate of others."
    elif my_type == '1' and their_type == '3':
        return "Type 1 individuals and Type 3 individuals can have a competitive relationship, as both types are ambitious and want to be successful. However, they can also learn from each other and support each other in achieving their goals if they are able to communicate openly and honestly."
    elif my_type == '1' and their_type == '4':
        return "Type 1 individuals and Type 4 individuals can have a challenging relationship, as they have different values and approaches to life. Type 1s value rationality and order, while Type 4s value individuality and emotion. However, they can also learn from each other and support each other if they are able to communicate openly and respect each other's differences."
    elif my_type == '1' and their_type == '5':
        return "Type 1 individuals and Type 5 individuals can have a good relationship, as they both value honesty and integrity. Type 1s can help Type 5s focus on their goals and be more organized, while Type 5s can help Type 1s be more objective and detached. They can support each other in achieving their goals if they are able to communicate openly and honestly."
    elif my_type == '1' and their_type == '6':
        return "Type 1 individuals and Type 6 individuals can have a supportive relationship, as they both value responsibility and hard work. Type 1s can help Type 6s be more confident and decisive, while Type 6s can help Type 1s be more flexible and adaptable. They can support each other in achieving their goals if they are able to communicate openly and honestly."
    elif my_type == '1' and their_type == '7':
        return "Type 1 individuals and Type 7 individuals can have a fun and lively relationship, as they both value excitement and adventure. Type 1s can help Type 7s be more organized and focused, while Type 7s can help Type 1s be more spontaneous and playful. They can support each other in achieving their goals if they are able to communicate openly and honestly."
    elif my_type == '1' and their_type == '8':
        return "Type 1 individuals and Type 8 individuals may have conflict due to their different values and approaches to life. Type 1s are focused on being fair and just, while Type 8s are focused on being assertive and in control. This can lead to disagreements and misunderstandings if they are not able to communicate and find common ground."
    elif my_type == '1' and their_type == '9':
        return "Type 1 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 1s tend to be more direct and confrontational, while Type 9s tend to be more laid back and avoid confrontation."
def generate_communication(my_type, their_type):
    if my_type == '2' and their_type == '1':
        return "Type 2 individuals and Type 1 individuals may have good communication if they are able to respect each other's boundaries and communicate their needs and expectations clearly. Type 2s tend to be more indirect and passive-aggressive, while Type 1s tend to be more direct and confrontational. By communicating openly and honestly, they can create a balanced and healthy relationship where both parties feel understood and valued."
    elif my_type == '2' and their_type == '2':
        return "Type 2 individuals and Type 2 individuals may have good communication if they are able to empathize with and validate each other's emotions. Both Type 2s tend to be emotionally sensitive and caring, which can lead to misunderstandings and conflicts if they are not able to communicate openly and honestly. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '2' and their_type == '3':
        return "Type 2 individuals and Type 3 individuals may have good communication if they are able to understand and appreciate each other's motivations and priorities. Type 2s value connection and intimacy, while Type 3s value success and recognition. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals."
    elif my_type == '2' and their_type == '4':
        return "Type 2 individuals and Type 4 individuals may have good communication if they are able to empathize with and validate each other's emotions. Type 2s tend to suppress their emotions, while Type 4s value and express their emotions. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '2' and their_type == '5':
        return "Type 2 individuals and Type 5 individuals may have good communication if they are able to respect each other's boundaries and communicate their needs and expectations clearly. Type 2s tend to be more emotionally sensitive and caring, while Type 5s tend to be more detached and independent. By communicating openly and honestly, they can create a balanced and healthy relationship where both parties feel understood and valued."
    elif my_type == '2' and their_type == '6':
        return "Type 2 individuals and Type 6 individuals may have good communication if they are able to trust each other and work together to overcome their shared anxiety and fear. Type 2s tend to be more emotionally sensitive and caring, while Type 6s tend to be more anxious and hesitant. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '2' and their_type == '7':
        return "Type 2 individuals and Type 7 individuals may have good communication if they are able to balance their different communication styles and find common ground. Type 2s tend to be more emotionally sensitive and caring, while Type 7s tend to be more lighthearted and playful. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
   elif my_type == '2' and their_type == '8':
        return "Type 2 individuals and Type 8 individuals may have good communication if they are able to respect each other's boundaries and communicate their needs and expectations clearly. Type 2s tend to be more indirect and passive-aggressive, while Type 8s tend to be more assertive and confrontational. By communicating openly and honestly, they can create a balanced and healthy relationship where both parties feel understood and valued."
    elif my_type == '2' and their_type == '9':
        return "Type 2 individuals and Type 9 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 2s tend to be more emotionally sensitive and caring, while Type 9s tend to be more passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
def generate_communication(my_type, their_type):
    if my_type == '3' and their_type == '1':
        return "Type 3 individuals and Type 1 individuals may have good communication if they are able to understand and appreciate each other's motivations and priorities. Type 3s value success and recognition, while Type 1s value fairness and justice. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals."
    elif my_type == '3' and their_type == '2':
        return "Type 3 individuals and Type 2 individuals may have good communication if they are able to understand and appreciate each other's motivations and priorities. Type 3s value success and recognition, while Type 2s value connection and intimacy. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals."
    elif my_type == '3' and their_type == '3':
        return "Type 3 individuals and Type 3 individuals may have good communication if they are able to support and motivate each other to achieve their shared goals. Both Type 3s value success and recognition, which can lead to competition and rivalry if they are not able to communicate openly and honestly. By communicating openly and positively, they can create a strong and supportive bond that helps them achieve their goals and grow together."
    elif my_type == '3' and their_type == '4':
        return "Type 3 individuals and Type 4 individuals may have good communication if they are able to understand and empathize with each other's emotional needs. Type 3s tend to suppress their emotions, while Type 4s value and express their emotions. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '3' and their_type == '5':
        return "Type 3 individuals and Type 5 individuals may have good communication if they are able to balance their different approaches to dealing with the world. Type 3s tend to be more proactive and involved, while Type 5s tend to be more detached and independent. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '3' and their_type == '6':
        return "Type 3 individuals and Type 6 individuals may have good communication if they are able to trust each other and work together to overcome their shared anxiety and fear. Type 3s tend to be more proactive and ambitious, while Type 6s tend to be more anxious and hesitant. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '3' and their_type == '7':
        return "Type 3 individuals and Type 7 individuals may have good communication if they are able to balance their different communication styles and find common ground. Type 3s tend to be more proactive and ambitious, while Type 7s tend to be more lighthearted and playful. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '3' and their_type == '8':
        return "Type 3 individuals and Type 8 individuals may have good communication if they are able to understand and appreciate each other's motivations and priorities. Type 3s value success and recognition, while Type 8s value power and control. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals."
    elif my_type == '3' and their_type == '9':
        return "Type 3 individuals and Type 9 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 3s tend to be more proactive and ambitious, while Type 9s tend to be more passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
def generate_communication(my_type, their_type):
    if my_type == '4' and their_type == '1':
        return "Type 4 individuals and Type 1 individuals may have good communication if they are able to understand and respect each other's emotional needs and values. Type 4s value and express their emotions, while Type 1s value fairness and justice. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '4' and their_type == '2':
        return "Type 4 individuals and Type 2 individuals may have good communication if they are able to understand and empathize with each other's emotional needs. Type 4s value and express their emotions, while Type 2s value connection and intimacy. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '4' and their_type == '3':
        return "Type 4 individuals and Type 3 individuals may have good communication if they are able to understand and empathize with each other's emotional needs. Type 4s value and express their emotions, while Type 3s tend to suppress their emotions. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '4' and their_type == '4':
        return "Type 4 individuals and Type 4 individuals may have good communication if they are able to understand and support each other's emotional needs and individuality. Both Type 4s value and express their emotions, which can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and honestly. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '4' and their_type == '5':
        return "Type 4 individuals and Type 5 individuals may have good communication if they are able to understand and respect each other's emotional needs and perspectives. Type 4s value and express their emotions, while Type 5s tend to suppress their emotions. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '4' and their_type == '6':
        return "Type 4 individuals and Type 6 individuals may have good communication if they are able to trust each other and work together to overcome their shared anxiety and fear. Type 4s value and express their emotions, while Type 6s tend to suppress their emotions. By communicating openly and vulnerably, they can create a safe and supportive space for each other to express their feelings and needs."
    elif my_type == '4' and their_type == '6':
        return "Type 4 individuals and Type 6 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 4s tend to be more sensitive and expressive, while Type 6s tend to be more anxious and hesitant. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '4' and their_type == '7':
        return "Type 4 individuals and Type 7 individuals may have good communication if they are able to balance their different communication styles and find common ground. Type 4s tend to be more sensitive and expressive, while Type 7s tend to be more lighthearted and playful. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '4' and their_type == '8':
        return "Type 4 individuals and Type 8 individuals may have good communication if they are able to understand and appreciate each other's emotional needs and motivations. Type 4s value and express their emotions, while Type 8s value power and control. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '4' and their_type == '9':
        return "Type 4 individuals and Type 9 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 4s tend to be more sensitive and expressive, while Type 9s tend to be more passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
def generate_communication(my_type, their_type):
    if my_type == '5' and their_type == '1':
        return "Type 5 individuals and Type 1 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 5s tend to be more detached and independent, while Type 1s tend to be more direct and confrontational. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '5' and their_type == '2':
        return "Type 5 individuals and Type 2 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 5s tend to be more detached and independent, while Type 2s tend to be more supportive and caring. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '5' and their_type == '3':
        return "Type 5 individuals and Type 3 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 5s tend to be more detached and independent, while Type 3s value success and recognition. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '5' and their_type == '4':
        return "Type 5 individuals and Type 4 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 5s tend to be more detached and independent, while Type 4s value and express their emotions. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '5' and their_type == '5':
        return "Type 5 individuals and Type 5 individuals may have good communication if they are able to respect each other's boundaries and independence. Both Type 5s tend to be detached and independent, which can lead to misunderstandings and resentment if they are not able to communicate openly and honestly. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '5' and their_type == '6':
        return "Type 5 individuals and Type 6 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 5s tend to be more detached and independent, while Type 6s tend to be more anxious and hesitant. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '5' and their_type == '7':
        return "Type 5 individuals and Type 7 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 5s tend to be more detached and independent, while Type 7s tend to be more lighthearted and playful. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '5' and their_type == '8':
        return "Type 5 individuals and Type 8 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 5s tend to be more detached and independent, while Type 8s value power and control. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '5' and their_type == '9':
        return "Type 5 individuals and Type 9 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 5s tend to be more detached and independent, while Type 9s tend to be more passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
def generate_communication(my_type, their_type):
    if my_type == '6' and their_type == '1':
        return "Type 6 individuals and Type 1 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 6s tend to be more anxious and hesitant, while Type 1s tend to be more direct and confrontational. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '6' and their_type == '2':
        return "Type 6 individuals and Type 2 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 6s tend to be more anxious and hesitant, while Type 2s tend to be more supportive and caring. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '6' and their_type == '3':
        return "Type 6 individuals and Type 3 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 6s tend to be more anxious and hesitant, while Type 3s value success and recognition. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '6' and their_type == '4':
        return "Type 6 individuals and Type 4 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 6s tend to be more anxious and hesitant, while Type 4s value and express their emotions. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '6' and their_type == '5':
        return "Type 6 individuals and Type 5 individuals may have good communication if they are able to respect each other's boundaries and independence. Type 6s tend to be anxious and hesitant, while Type 5s tend to be detached and independent. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '6' and their_type == '6':
        return "Type 6 individuals and Type 6 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Both Type 6s tend to be anxious and hesitant, which can lead to misunderstandings and resentment if they are not able to communicate openly and honestly. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '6' and their_type == '7':
        return "Type 6 individuals and Type 7 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 6s tend to be more anxious and hesitant, while Type 7s tend to be more lighthearted and playful. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '6' and their_type == '8':
        return "Type 6 individuals and Type 8 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 6s tend to be more anxious and hesitant, while Type 8s value power and control. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '6' and their_type == '9':
        return "Type 6 individuals and Type 9 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 6s tend to be more anxious and hesitant, while Type 9s tend to be more passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '6' and their_type == '7':
        return "Type 6 individuals and Type 7 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 6s tend to be more anxious and hesitant, while Type 7s tend to be more lighthearted and playful. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '6' and their_type == '8':
        return "Type 6 individuals and Type 8 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 6s tend to be more anxious and hesitant, while Type 8s value power and control. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '6' and their_type == '9':
        return "Type 6 individuals and Type 9 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 6s tend to be more anxious and hesitant, while Type 9s tend to be more passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
def generate_communication(my_type, their_type):
    if my_type == '7' and their_type == '1':
        return "Type 7 individuals and Type 1 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 7s tend to be more lighthearted and playful, while Type 1s tend to be more direct and confrontational. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '7' and their_type == '2':
        return "Type 7 individuals and Type 2 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 7s tend to be more lighthearted and playful, while Type 2s tend to be more supportive and caring. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '7' and their_type == '3':
        return "Type 7 individuals and Type 3 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 7s tend to be more lighthearted and playful, while Type 3s value success and recognition. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '7' and their_type == '4':
        return "Type 7 individuals and Type 4 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 7s tend to be more lighthearted and playful, while Type 4s value and express their emotions. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '7' and their_type == '5':
        return "Type 7 individuals and Type 5 individuals may have good communication if they are able to respect each other's boundaries and independence. Type 7s tend to be lighthearted and playful, while Type 5s tend to be detached and independent. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '7' and their_type == '6':
        return "Type 7 individuals and Type 6 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 7s tend to be more lighthearted and playful, while Type 6s tend to be anxious and hesitant. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '7' and their_type == '8':
        return "Type 7 individuals and Type 8 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 7s tend to be more lighthearted and playful, while Type 8s value power and control. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '7' and their_type == '9':
        return "Type 7 individuals and Type 9 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 7s tend to be more lighthearted and playful, while Type 9s tend to be passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
def generate_communication(my_type, their_type):
    if my_type == '8' and their_type == '1':
        return "Type 8 individuals and Type 1 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 8s value power and control, while Type 1s tend to be direct and confrontational. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '8' and their_type == '2':
        return "Type 8 individuals and Type 2 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 8s value power and control, while Type 2s tend to be supportive and caring. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '8' and their_type == '3':
        return "Type 8 individuals and Type 3 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 8s value power and control, while Type 3s value success and recognition. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '8' and their_type == '4':
        return "Type 8 individuals and Type 4 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 8s value power and control, while Type 4s value and express their emotions. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '8' and their_type == '5':
        return "Type 8 individuals and Type 5 individuals may have good communication if they are able to respect each other's boundaries and independence. Type 8s value power and control, while Type 5s tend to be detached and independent. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '8' and their_type == '6':
        return "Type 8 individuals and Type 6 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 8s value power and control, while Type 6s tend to be anxious and hesitant. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '8' and their_type == '7':
        return "Type 8 individuals and Type 7 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 8s value power and control, while Type 7s tend to be lighthearted and playful. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '8' and their_type == '8':
        return "Type 8 individuals and Type 8 individuals may have good communication if they are able to trust each other and support each other's goals and needs. Both value power and control, and can benefit from each other's experiences and perspectives. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '8' and their_type == '9':
        return "Type 8 individuals and Type 9 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 8s value power and control, while Type 9s tend to be passive and accommodating. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
def generate_communication(my_type, their_type):
    if my_type == '9' and their_type == '1':
        return "Type 9 individuals and Type 1 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 9s tend to be passive and accommodating, while Type 1s tend to be direct and confrontational. By communicating openly and respectfully, they can learn from each other's perspectives and find ways to support each other's goals and needs."
    elif my_type == '9' and their_type == '2':
        return "Type 9 individuals and Type 2 individuals may have good communication if they are able to trust each other and support each other's emotional needs. Type 9s tend to be passive and accommodating, while Type 2s tend to be supportive and caring. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '9' and their_type == '3':
        return "Type 9 individuals and Type 3 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 9s tend to be passive and accommodating, while Type 3s value success and recognition. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '9' and their_type == '4':
        return "Type 9 individuals and Type 4 individuals may have good communication if they are able to listen to each other's perspectives and find common ground. Type 9s tend to be passive and accommodating, while Type 4s value and express their emotions. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '9' and their_type == '5':
        return "Type 9 individuals and Type 5 individuals may have good communication if they are able to respect each other's boundaries and independence. Type 9s tend to be passive and accommodating, while Type 5s tend to be detached and independent. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '9' and their_type == '6':
        return "Type 9 individuals and Type 6 individuals may have good communication if they are able to balance their different communication styles and priorities. Type 9s tend to be passive and accommodating, while Type 6s tend to be loyal and supportive. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '9' and their_type == '7':
        return "Type 9 individuals and Type 7 individuals may have good communication if they are able to respect each other's boundaries and independence. Type 9s tend to be passive and accommodating, while Type 7s tend to be spontaneous and adventurous. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
    elif my_type == '9' and their_type == '8':
        return "Type 9 individuals and Type 8 individuals may have good communication if they are able to understand and appreciate each other's perspectives and motivations. Type 9s tend to be passive and accommodating, while Type 8s value power and control. By communicating openly and respectfully, they can learn from each other's experiences and find ways to support each other's goals and needs."
    elif my_type == '9' and their_type == '9':
        return "Type 9 individuals and Type 9 individuals may have good communication if they are able to trust each other and support each other's goals and needs. Both tend to be passive and accommodating, and can benefit from each other's experiences and perspectives. By communicating openly and honestly, they can create a strong and supportive bond that helps them overcome their challenges and grow together."
def generate_conflict(my_type, their_type):
    if my_type == '1' and their_type == '2':
        return "Type 1 individuals and Type 2 individuals may have conflict due to their different communication styles. Type 1s tend to be more direct and confrontational, while Type 2s tend to be more indirect and passive-aggressive. This can lead to misunderstandings and resentment if they are not able to communicate openly and resolve conflicts constructively."
    elif my_type == '1' and their_type == '3':
        return "Type 1 individuals and Type 3 individuals may have conflict due to their different priorities and motivations. Type 1s value fairness and justice, while Type 3s value success and recognition. This can lead to disagreements and competition if they are not able to communicate openly and find common ground."
    elif my_type == '1' and their_type == '4':
        return "Type 1 individuals and Type 4 individuals may have conflict due to their different emotional needs. Type 1s tend to suppress their emotions, while Type 4s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '1' and their_type == '5':
        return "Type 1 individuals and Type 5 individuals may have conflict due to their different approaches to dealing with the world. Type 1s tend to be more proactive and involved, while Type 5s tend to be more detached and independent. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's differences."
    elif my_type == '1' and their_type == '6':
        return "Type 1 individuals and Type 6 individuals may have conflict due to their different coping mechanisms. Type 1s tend to use denial and rationalization, while Type 6s tend to use anxiety and doubt. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '1' and their_type == '7':
        return "Type 1 individuals and Type 7 individuals may have conflict due to their different priorities and values. Type 1s value fairness and justice, while Type 7s value freedom and excitement. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '1' and their_type == '8':
        return "Type 1 individuals and Type 8 individuals may have conflict due to their different communication styles and values. Type 1s tend to be more rational and objective, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '1' and their_type == '9':
        return "Type 1 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 1s tend to be more direct and confrontational, while Type 9s tend to be more passive and avoidant. This can lead to misunderstandings and resentment if they are not able to communicate openly and listen to each other's perspectives."

def generate_conflict(my_type, their_type):
    if my_type == '2' and their_type == '1':
        return "Type 2 individuals and Type 1 individuals may have conflict due to their different communication styles. Type 2s tend to be more indirect and passive-aggressive, while Type 1s tend to be more direct and confrontational. This can lead to misunderstandings and resentment if they are not able to communicate openly and resolve conflicts constructively."
    elif my_type == '2' and their_type == '3':
        return "Type 2 individuals and Type 3 individuals may have conflict due to their different priorities and motivations. Type 2s value validation and recognition, while Type 3s value success and recognition. This can lead to competition and jealousy if they are not able to communicate openly and support each other in achieving their goals."
    elif my_type == '2' and their_type == '4':
        return "Type 2 individuals and Type 4 individuals may have conflict due to their different emotional needs. Type 2s tend to suppress their emotions and focus on others, while Type 4s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '2' and their_type == '5':
        return "Type 2 individuals and Type 5 individuals may have conflict due to their different approaches to dealing with the world. Type 2s tend to be more involved and interactive, while Type 5s tend to be more detached and independent. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '2' and their_type == '6':
        return "Type 2 individuals and Type 6 individuals may have conflict due to their different coping mechanisms. Type 2s tend to use validation-seeking and avoidance, while Type 6s tend to use anxiety and doubt. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '2' and their_type == '7':
        return "Type 2 individuals and Type 7 individuals may have conflict due to their different priorities and values. Type 2s value validation and recognition, while Type 7s value freedom and excitement. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '2' and their_type == '8':
        return "Type 2 individuals and Type 8 individuals may have conflict due to their different communication styles and values. Type 2s tend to be more passive-aggressive and manipulative, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '2' and their_type == '9':
        return "Type 2 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 2s tend to be more indirect and passive-aggressive, while Type 9s tend to be more passive and avoidant. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."

def generate_conflict(my_type, their_type):
    if my_type == '3' and their_type == '1':
        return "Type 3 individuals and Type 1 individuals may have conflict due to their different priorities and motivations. Type 3s value success and recognition, while Type 1s value fairness and justice. This can lead to disagreements and competition if they are not able to communicate openly and find common ground."
    elif my_type == '3' and their_type == '2':
        return "Type 3 individuals and Type 2 individuals may have conflict due to their different priorities and motivations. Type 3s value success and recognition, while Type 2s value validation and recognition. This can lead to competition and jealousy if they are not able to communicate openly and support each other in achieving their goals."
    elif my_type == '3' and their_type == '4':
        return "Type 3 individuals and Type 4 individuals may have conflict due to their different emotional needs. Type 3s tend to suppress their emotions and focus on achieving their goals, while Type 4s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '3' and their_type == '5':
        return "Type 3 individuals and Type 5 individuals may have conflict due to their different approaches to dealing with the world. Type 3s tend to be more involved and interactive, while Type 5s tend to be more detached and independent. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '3' and their_type == '6':
        return "Type 3 individuals and Type 6 individuals may have conflict due to their different coping mechanisms. Type 3s tend to use denial and rationalization, while Type 6s tend to use anxiety and doubt. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '3' and their_type == '7':
        return "Type 3 individuals and Type 7 individuals may have conflict due to their different priorities and values. Type 3s value success and recognition, while Type 7s value freedom and excitement. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '3' and their_type == '8':
        return "Type 3 individuals and Type 8 individuals may have conflict due to their different communication styles and values. Type 3s tend to be more charming and manipulative, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '3' and their_type == '9':
        return "Type 3 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 3s tend to be more assertive and focused on achieving their goals, while Type 9s tend to be more passive and avoidant. This can lead to misunderstandings and resentment if they are not able to communicate openly and listen to each other's perspectives."

def generate_conflict(my_type, their_type):
    if my_type == '4' and their_type == '1':
        return "Type 4 individuals and Type 1 individuals may have conflict due to their different emotional needs. Type 4s value and express their emotions, while Type 1s tend to suppress their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '4' and their_type == '2':
        return "Type 4 individuals and Type 2 individuals may have conflict due to their different emotional needs. Type 4s value and express their emotions, while Type 2s tend to suppress their emotions and focus on others. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '4' and their_type == '3':
        return "Type 4 individuals and Type 3 individuals may have conflict due to their different emotional needs. Type 4s value and express their emotions, while Type 3s tend to suppress their emotions and focus on achieving their goals. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '4' and their_type == '5':
        return "Type 4 individuals and Type 5 individuals may have conflict due to their different approaches to dealing with the world. Type 4s tend to be more involved and interactive, while Type 5s tend to be more detached and independent. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '4' and their_type == '6':
        return "Type 4 individuals and Type 6 individuals may have conflict due to their different coping mechanisms. Type 4s tend to use emotional expression and avoidance, while Type 6s tend to use anxiety and doubt. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '4' and their_type == '7':
        return "Type 4 individuals and Type 7 individuals may have conflict due to their different priorities and values. Type 4s value emotional depth and authenticity, while Type 7s value freedom and excitement. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '4' and their_type == '8':
        return "Type 4 individuals and Type 8 individuals may have conflict due to their different communication styles and values. Type 4s tend to be more introspective and sensitive, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '4' and their_type == '9':
        return "Type 4 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 4s tend to be more emotional and reactive, while Type 9s tend to be more passive and avoidant. This can lead to misunderstandings and resentment if they are not able to communicate openly and listen to each other's perspectives."

def generate_conflict(my_type, their_type):
    if my_type == '5' and their_type == '1':
        return "Type 5 individuals and Type 1 individuals may have conflict due to their different approaches to dealing with the world. Type 5s tend to be more detached and independent, while Type 1s tend to be more proactive and involved. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's differences."
    elif my_type == '5' and their_type == '2':
        return "Type 5 individuals and Type 2 individuals may have conflict due to their different approaches to dealing with the world. Type 5s tend to be more detached and independent, while Type 2s tend to be more involved and interactive. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '5' and their_type == '3':
        return "Type 5 individuals and Type 3 individuals may have conflict due to their different approaches to dealing with the world. Type 5s tend to be more detached and independent, while Type 3s tend to be more involved and interactive. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '5' and their_type == '4':
        return "Type 5 individuals and Type 4 individuals may have conflict due to their different approaches to dealing with the world. Type 5s tend to be more detached and independent, while Type 4s tend to be more involved and interactive. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '5' and their_type == '6':
        return "Type 5 individuals and Type 6 individuals may have conflict due to their different coping mechanisms. Type 5s tend to use detachment and intellectualization, while Type 6s tend to use anxiety and doubt. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '5' and their_type == '7':
        return "Type 5 individuals and Type 7 individuals may have conflict due to their different priorities and values. Type 5s value knowledge and understanding, while Type 7s value freedom and excitement. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '5' and their_type == '8':
        return "Type 5 individuals and Type 8 individuals may have conflict due to their different communication styles and values. Type 5s tend to be more detached and independent, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '5' and their_type == '9':
        return "Type 5 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 5s tend to be more detached and analytical, while Type 9s tend to be more passive and avoidant. This can lead to misunderstandings and resentment if they are not able to communicate openly and listen to each other's perspectives"

def generate_conflict(my_type, their_type):
    if my_type == '6' and their_type == '1':
        return "Type 6 individuals and Type 1 individuals may have conflict due to their different coping mechanisms. Type 6s tend to use anxiety and doubt, while Type 1s tend to use anger and criticism. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '6' and their_type == '2':
        return "Type 6 individuals and Type 2 individuals may have conflict due to their different emotional needs. Type 6s tend to suppress their emotions and focus on others, while Type 2s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '6' and their_type == '3':
        return "Type 6 individuals and Type 3 individuals may have conflict due to their different priorities and motivations. Type 6s value security and stability, while Type 3s value success and recognition. This can lead to disagreements and competition if they are not able to communicate openly and find common ground."
    elif my_type == '6' and their_type == '4':
        return "Type 6 individuals and Type 4 individuals may have conflict due to their different coping mechanisms. Type 6s tend to use anxiety and doubt, while Type 4s tend to use emotional expression and avoidance. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '6' and their_type == '5':
        return "Type 6 individuals and Type 5 individuals may have conflict due to their different coping mechanisms. Type 6s tend to use anxiety and doubt, while Type 5s tend to use detachment and intellectualization. This can lead to misunderstandings and insecurity if they are not able to communicate openly and support each other in overcoming their fears."
    elif my_type == '6' and their_type == '7':
        return "Type 6 individuals and Type 7 individuals may have conflict due to their different priorities and values. Type 6s value security and stability, while Type 7s value freedom and excitement. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '6' and their_type == '8':
        return "Type 6 individuals and Type 8 individuals may have conflict due to their different communication styles and values. Type 6s tend to be more anxious and hesitant, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '6' and their_type == '9':
        return "Type 6 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 6s tend to be more anxious and reactive, while Type 9s tend to be more passive and avoidant. This can lead to misunderstandings and resentment if they are not able to communicate openly and listen to each other's perspectives."


def generate_conflict(my_type, their_type):
    if my_type == '7' and their_type == '1':
        return "Type 7 individuals and Type 1 individuals may have conflict due to their different priorities and values. Type 7s value freedom and excitement, while Type 1s value fairness and justice. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '7' and their_type == '2':
        return "Type 7 individuals and Type 2 individuals may have conflict due to their different emotional needs. Type 7s tend to suppress their emotions and focus on the future, while Type 2s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '7' and their_type == '3':
        return "Type 7 individuals and Type 3 individuals may have conflict due to their different priorities and motivations. Type 7s value freedom and excitement, while Type 3s value success and recognition. This can lead to disagreements and competition if they are not able to communicate openly and find common ground."
    elif my_type == '7' and their_type == '4':
        return "Type 7 individuals and Type 4 individuals may have conflict due to their different emotional needs. Type 7s tend to suppress their emotions and focus on the future, while Type 4s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '7' and their_type == '5':
        return "Type 7 individuals and Type 5 individuals may have conflict due to their different priorities and values. Type 7s value freedom and excitement, while Type 5s value knowledge and understanding. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '7' and their_type == '6':
        return "Type 7 individuals and Type 6 individuals may have conflict due to their different priorities and values. Type 7s value freedom and excitement, while Type 6s value security and stability. This can lead to disagreements and tension if they are not able to communicate openly and find common ground."
    elif my_type == '7' and their_type == '8':
        return "Type 7 individuals and Type 8 individuals may have conflict due to their different communication styles and values. Type 7s tend to be more lighthearted and playful, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '7' and their_type == '9':
        return "Type 7 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with emotions. Type 7s tend to be more lighthearted and playful, while Type 9s tend to be more passive and avoidant. This can lead to misunderstandings and resentment if they are not able to communicate openly and listen to each other's perspectives."

def generate_conflict(my_type, their_type):
    if my_type == '8' and their_type == '1':
        return "Type 8 individuals and Type 1 individuals may have conflict due to their different communication styles and values. Type 8s tend to be more assertive and confrontational, while Type 1s tend to be more direct and confrontational. This can lead to misunderstandings and resentment if they are not able to communicate openly and resolve conflicts constructively."
    elif my_type == '8' and their_type == '2':
        return "Type 8 individuals and Type 2 individuals may have conflict due to their different emotional needs. Type 8s tend to suppress their emotions and focus on control, while Type 2s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '8' and their_type == '3':
        return "Type 8 individuals and Type 3 individuals may have conflict due to their different priorities and motivations. Type 8s value power and control, while Type 3s value success and recognition. This can lead to disagreements and competition if they are not able to communicate openly and find common ground."
    elif my_type == '8' and their_type == '4':
        return "Type 8 individuals and Type 4 individuals may have conflict due to their different emotional needs. Type 8s tend to suppress their emotions and focus on control, while Type 4s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '8' and their_type == '5':
        return "Type 8 individuals and Type 5 individuals may have conflict due to their different communication styles and values. Type 8s tend to be more assertive and confrontational, while Type 5s tend to be more detached and independent. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '8' and their_type == '6':
        return "Type 8 individuals and Type 6 individuals may have conflict due to their different communication styles and values. Type 8s tend to be more assertive and confrontational, while Type 6s tend to be more anxious and hesitant. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '8' and their_type == '7':
        return "Type 8 individuals and Type 7 individuals may have conflict due to their different communication styles and values. Type 7s tend to be more lighthearted and playful, while Type 8s tend to be more assertive and confrontational. This can lead to misunderstandings and power struggles if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '8' and their_type == '9':
        return "Type 8 individuals and Type 9 individuals may have conflict due to their different approaches to dealing with power and control. Type 9s tend to avoid conflicts and suppress their emotions, while Type 8s tend to assert themselves and confront others. This can lead to misunderstandings and resentment if they are not able to communicate openly and resolve conflicts constructively."

def generate_conflict(my_type, their_type):
    if my_type == '9' and their_type == '1':
        return "Type 9 individuals and Type 1 individuals may have conflict due to their different communication styles and values. Type 9s tend to be more passive and accommodating, while Type 1s tend to be more direct and confrontational. This can lead to misunderstandings and resentment if they are not able to communicate openly and resolve conflicts constructively."
    elif my_type == '9' and their_type == '2':
        return "Type 9 individuals and Type 2 individuals may have conflict due to their different emotional needs. Type 9s tend to suppress their emotions and avoid conflict, while Type 2s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '9' and their_type == '3':
        return "Type 9 individuals and Type 3 individuals may have conflict due to their different priorities and motivations. Type 9s value peace and harmony, while Type 3s value success and recognition. This can lead to disagreements and competition if they are not able to communicate openly and find common ground."
    elif my_type == '9' and their_type == '4':
        return "Type 9 individuals and Type 4 individuals may have conflict due to their different emotional needs. Type 9s tend to suppress their emotions and avoid conflict, while Type 4s value and express their emotions. This can lead to misunderstandings and emotional outbursts if they are not able to communicate openly and empathize with each other."
    elif my_type == '9' and their_type == '5':
        return "Type 9 individuals and Type 5 individuals may have conflict due to their different communication styles and values. Type 9s tend to be more passive and accommodating, while Type 5s tend to be more detached and independent. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's boundaries."
    elif my_type == '9' and their_type == '6':
        return "Type 9 individuals and Type 6 individuals may have conflict due to their different communication styles and values. Type 9s tend to be more passive and accommodating, while Type 6s tend to be more anxious and hesitant. This can lead to misunderstand
    elif my_type == '9' and their_type == '7':
        return "Type 9 individuals and Type 7 individuals may have conflict due to their different communication styles and priorities. Type 9s tend to be more passive and accommodating, while Type 7s tend to be more lighthearted and playful. This can lead to misunderstandings and resentment if they are not able to communicate openly and respect each other's needs and boundaries."
    elif my_type == '9' and their_type == '8':
        return "Type 9 individuals and Type 8 individuals may have conflict due to their different approaches to dealing with power and control. Type 9s tend to avoid conflicts and suppress their emotions, while Type 8s tend to assert themselves and confront others. This can lead to misunderstandings and resentment if they are not able to communicate openly and resolve conflicts constructively."
    elif my_type == '9' and their_type == '9':
        return "Type 9 individuals and Type 9 individuals may have conflict due to their shared tendency to avoid conflicts and suppress their emotions. Both Type 9s value peace and harmony, which can lead to misunderstandings and resentment if they are not able to communicate openly and honestly. By communicating openly and positively, they can create a strong and supportive bond that helps them overcome their challenges and grow together."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect user input from the form
        my_type = request.form['my_type']
        their_type = request.form['their_type']

        # Generate the information to display on the page
        about_my_type = generate_about_my_type(my_type)
        about_their_type = generate_about_their_type(their_type)
        communication = generate_communication(my_type, their_type)
        conflict = generate_conflict(my_type, their_type)

        # Render the results page with the generated information
        return render_template('results.html', about_my_type=about_my_type, about_their_type=about_their_type, communication=communication, conflict=conflict)
    else:
        # Render the initial form
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
