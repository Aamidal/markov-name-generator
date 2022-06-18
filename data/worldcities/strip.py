import os

script_dir = os.path.dirname(__file__)
save_path = "data/places_aamidal.txt"
abs_save_path = os.path.join(script_dir, save_path)

places =['Abarra', 'Guparta', 'Koyo Isu', 'Bozeg', 'Phodai', 'Teraat', 'Qabis',
'Chakiragar', 'Tismin Insu', 'Kalmoro', 'Ethar', 'Kotelga', 'Altaxa', 'Nebay',
'Nebayanat', 'Aamidal', 'Standing', 'Bhidra', 'Oret Soi', 'Sudarai', 'Bhojo Patal',
'Matra Dhor',  'Niyat Dhor', 'Grahisa', 'Kono Manoi', 'Turagai', 'Jamosom', 'Ekanga',
'Desh', 'Yaburah', 'Tsugge', 'Harai', 'Rumid', 'Siur', 'Ksu', 'Vo', 'Su', 'Kusaslu',
'Bhanusri', 'Nasiraat', 'Santhe', 'Sestab','Kano Insu', 'Kusequ', 'Kanoyariya', 
'Turaatrah', 'Guparahid', 'Joyen Bor']

with open(abs_save_path, 'w') as f:
    for name in places:
        f.write(name + '\n')

