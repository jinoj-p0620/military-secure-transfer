import os
from datetime import datetime
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Crypto.PublicKey import RSA

# Create your views here.
from military import settings
from myapp.models import *

def Logout(request):
    logout(request)
    return render(request,'login.html')

def login_get(request):
    return render(request,'login.html')
def login_post(request):
    username = request.POST['email']
    password = request.POST['pass']
    user = authenticate(request,username = username,password = password)
    if user is not None:
        if user.groups.filter(name="Admin").exists():
            login(request,user)
            return redirect('/myapp/adminhome/')

        elif user.groups.filter(name="staff").exists():
            login(request,user)
            return redirect('/myapp/staff_home/')
        else:
            return redirect('/myapp/login/')
    else:
        return redirect('/myapp/login/')

def adminhome_get(request):
    return render(request, 'Admin/adminhome.html')

def add_department(request):
    return render(request,'Admin/Add department.html')
def add_dept_post(request):
    dept=request.POST['name']
    a=Department()
    a.department_name=dept
    a.save()
    return redirect('/myapp/view_department/#ab')

def edit_department(request,id):
    a=Department.objects.get(id=id)
    return render(request,'Admin/Edit department.html',{"data":a})

def edit_dept_post(request):
    dept=request.POST['textfield']
    id=request.POST['id']

    a = Department.objects.get(id=id)
    a.department_name = dept
    a.save()
    return redirect('/myapp/view_department/#ab')




def delete_department(request,id):
    Department.objects.filter(id=id).delete()
    return redirect('/myapp/view_department/#ab')


def delete_notification(request,id):
    Notification.objects.filter(id=id).delete()
    return redirect('/myapp/view_notification/#ab')

def add_designation(request):
    return render(request,'Admin/Add designation.html')

def add_designation_post(request):
    designation=request.POST['name']

    a=Designation()
    a.designation=designation
    a.save()
    return redirect('/myapp/view_designation/#ab')

def delete_designation(request,id):
    Designation.objects.filter(id=id).delete()
    return redirect('/myapp/view_designation/#ab')

def delete_staff(request,id):
    staff.objects.filter(LOGIN=id).delete()
    User.objects.filter(id=id).delete()
    return redirect('/myapp/view_staff/#ab')
def delete_soldier(request,id):
    Soldier_table.objects.filter(LOGIN=id).delete()
    User.objects.filter(id=id).delete()
    return redirect('/myapp/view_soldier_dep/#ab')




def edit_designation(request,id):
    request.session['id']=id
    a=Designation.objects.get(id=id)
    return render(request,'Admin/Edit designation.html',{"data":a})

def edit_designation_post(request):
    designation=request.POST['name']

    a =Designation.objects.get(id=request.session['id'])
    a.designation =designation
    a.save()
    return redirect('/myapp/view_designation/#ab')

def send_notification(request):
    return render(request,'Admin/Send notification.html')

def send_notification_post(request):
    title = request.POST['title']
    description = request.POST['description']

    a = Notification()
    a.Title = title
    a.desc = description
    a.date=datetime.today()
    a.save()
    return redirect('/myapp/view_notification/#ab')

def view_department(request):
    a=Department.objects.all()
    return render(request,'Admin/view department.html',{"data":a})

def view_notification(request):
    ob=Notification.objects.all()
    return render(request,'Admin/View notification.html',{"data":ob})

def view_reply(request):
    K=complaints.objects.all()
    return render(request,'Admin/View reply.html',{"data":K})

def send_reply(request,id):
    request.session['compid']=id
    return render(request,'Admin/send reply.html')

def send_reply_post(request):
    reply=request.POST['reply']
    obj=complaints.objects.get(id=request.session['compid'])
    obj.Reply=reply
    obj.save()
    return redirect('/myapp/view_reply/#ab')

def view_designation(request):
    a=Designation.objects.all()
    return render(request,'Admin/View designation.html',{"data":a})

def view_soldier_admin(request):
    a=Soldier_table.objects.all()
    return render(request,'Admin/View soldier admin.html',{"data":a})

def add_soldier(request):
    a=Department.objects.all()
    b=Designation.objects.all()
    return render(request, 'Staff/Add soldier.html', {'data':a,'data2':b})

def  add_soldier_post(request):
    name=request.POST['textfield']
    photo=request.FILES['Photo']
    designation=request.POST['select2']
    email=request.POST['Email']
    gender=request.POST['gender']
    phone=request.POST['Phone']
    pincode=request.POST['Pincode']
    dob=request.POST['Dob']
    username=request.POST['Username']
    password=request.POST['Password']

    user = User.objects.create_user(username=username, password=password)
    user.save()
    user.groups.add(Group.objects.get(name="Soldier"))

    key = RSA.generate(2048)
    private_key=key.export_key().decode("utf-8")
    public_key=key.publickey().export_key().decode("utf-8")

    a=Soldier_table()
    a.STAFF = staff.objects.get(LOGIN=request.user.id)
    a.soldier_name=name
    a.soldier_image=photo
    a.DESIGNATION_id=designation
    a.email=email
    a.gender=gender
    a.phone=phone
    a.pincode=pincode
    a.dob=dob
    a.LOGIN=user
    a.private_key=private_key
    a.public_key=public_key
    a.save()
    return redirect('/myapp/view_soldier_dep/#ab')


def add_staff_get(request):
    a=Department.objects.all()
    return render(request,"Admin/Add staff.html",{"data":a})

def add_staff_post(request):
    department=request.POST['select']
    name=request.POST['name']
    place=request.POST['place']
    post=request.POST['post']
    email=request.POST['email']
    phone=request.POST['phone']
    pincode=request.POST['pincode']
    username=request.POST['username']
    password=request.POST['password']
    photo=request.FILES['photo']

    user=User.objects.create_user(username=username,password=password)
    user.save()
    user.groups.add(Group.objects.get(name="staff"))


    a=staff()
    a.name=name
    a.place=place
    a.post=post
    a.email=email
    a.phone=phone
    a.pincode=pincode
    a.photo=photo
    a.DEPARTMENT_id=department
    a.LOGIN=user
    a.save()
    return redirect('/myapp/view_staff/#ab')

def view_staff(request):
    a=staff.objects.all()
    return render(request,'Admin/View staff.html',{"data":a})


def edit_staff_get(request,id):
    a=Department.objects.all()
    s=staff.objects.get(id=id)
    request.session['staffid']=id
    return render(request,"Admin/Edit staff.html",{"data":a,'data2':s})

def edit_staff_post(request):
    department=request.POST['select']
    name=request.POST['name']
    place=request.POST['place']
    post=request.POST['post']
    email=request.POST['email']
    phone=request.POST['phone']
    pincode=request.POST['pincode']


    a=staff.objects.get(id=request.session['staffid'])
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        a.photo=photo
        a.save()

    a.name=name
    a.place=place
    a.post=post
    a.email=email
    a.phone=phone
    a.pincode=pincode
    a.DEPARTMENT_id=department
    a.save()
    return redirect('/myapp/view_staff/#ab')



def edit_soldier(request,id):
    b=Designation.objects.all()
    s = Soldier_table.objects.get(id=id)
    request.session['soldierid'] = id
    return render(request, 'Staff/Edit soldier.html',{"data":s,"data2":b})

def edit_soldier_post(request):
    name = request.POST['textfield']
    designation = request.POST['designation']
    email = request.POST['Email']
    gender = request.POST['gender']
    phone = request.POST['Phone']
    pincode = request.POST['Pincode']
    dob = request.POST['Dob']

    a = Soldier_table.objects.get(id=request.session['soldierid'])
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        a.soldier_image = photo
        a.save()
    a.soldier_name = name
    a.DESIGNATION_id = designation
    a.email = email
    a.gender = gender
    a.phone = phone
    a.pincode = pincode
    a.dob = dob
    a.save()
    return redirect('/myapp/view_soldier_dep/#ab')

def send_complaint(request):
    return render(request, 'Staff/Send complaint.html')

def send_complaint_post(request):
    compl=request.POST['complaint']
    a=complaints()
    a.Complaint_des=compl
    a.Reply='pending'
    a.LOGIN=User.objects.get(id=request.user.id)
    a.date=datetime.now()
    a.save()
    return redirect('/myapp/send_complaint/#ab')

def view_notification_dep(request):
    b=Notification.objects.all()
    return render(request, 'Staff/View notification_dep.html', {"data":b})

def view_reply_dep(request):
    b = complaints.objects.filter(LOGIN=request.user.id)
    return render(request, 'Staff/View reply_dep.html', {"data":b})

def view_soldier_dep(request):
    b = Soldier_table.objects.filter(STAFF__LOGIN=request.user.id)
    return render(request,'Staff/view soldier_dep.html',{"data":b})

def staff_home(request):
    return render(request, 'Staff/department index.html')

def view_soldier_upload(request):
    b = Soldier_table.objects.all()
    return render(request, 'Staff/view soldier_upload.html',{"data":b})

def upload_file(request,id):
    request.session['sol_id']=id
    return render(request,'Staff/upload_file.html')

def upload_file_post(request):
    solid=request.session['sol_id']
    file=request.FILES['file']
    msg=request.POST['msg']
    return redirect('/myapp/view_soldier_upload/#ab')


#===========================================================================================
#===========================================================================================
#===========================================================================================
#===========================================================================================

def flutterlogin(request):
    username = request.POST['uname']
    password = request.POST['psw']
    user = authenticate(request,username = username,password = password)
    if user is not None:
        if user.groups.filter(name="Soldier").exists():
            login(request,user)
            return JsonResponse({"status":"ok","lid":str(user.id),"type":"Soldier"})
        else:
            return JsonResponse({"status":"notok"})
    else:
        return JsonResponse({"status":"invalid"})

def sol_view_notification(request):
    ob=Notification.objects.all()
    l=[]
    for i in ob:
        l.append({"id":str(i.id),
                  "Title":i.Title,
                  "desc":i.desc,
                  "date":str(i.date),
                  })
    return JsonResponse({"status":"ok","data":l})

def sol_send_complaint_post(request):
    compl=request.POST['complaint']
    lid=request.POST['lid']
    a=complaints()
    a.Complaint_des=compl
    a.Reply='pending'
    a.LOGIN=User.objects.get(id=lid)
    a.date=datetime.now()
    a.save()
    return JsonResponse({"status": "ok"})

def sol_view_reply(request):
    lid=request.POST['lid']
    ob = complaints.objects.filter(LOGIN=lid)
    A = []
    for i in ob:
        A.append({"id": str(i.id),
                  "Complaint_des": i.Complaint_des,
                  "Reply": i.Reply,
                  "date": str(i.date),
                  })
    print(A)
    return JsonResponse({"status": "ok","data":A})


def sol_view_profile(request):
    try:
        lid = request.POST['lid']
        ob = Soldier_table.objects.get(LOGIN=lid)
        data = {
            "id": str(ob.id),
            "name": ob.soldier_name,
            "desi": ob.DESIGNATION.designation,
            "dept": ob.STAFF.DEPARTMENT.department_name,
            "img": ob.soldier_image.url if ob.soldier_image else "",
            "email": ob.email,
            "gender": ob.gender,
            "phone": str(ob.phone),
            "pincode": str(ob.pincode),
            "dob": str(ob.dob),
        }
        return JsonResponse({"status": "ok", "data": data})
    except Soldier_table.DoesNotExist:
        return JsonResponse({"status": "error", "msg": "Soldier not found"})
    except Exception as e:
        return JsonResponse({"status": "error", "msg": str(e)})

def soldier_view_soldiers(request):
    try:
        lid = request.POST['lid']
        ob = Soldier_table.objects.all().exclude(LOGIN=lid)

        soldier_list = []
        for i in ob:
            image_url = ""
            if i.soldier_image:
                image_url = request.build_absolute_uri(i.soldier_image.url)
            soldier_list.append({
                "id": str(i.id),
                "name": i.soldier_name,
                "department": i.STAFF.DEPARTMENT.department_name,
                "email": i.email,
                "phone": str(i.phone),
                "gender": i.gender,
                "dob": str(i.dob),
                "pincode": str(i.pincode),
                "designation": i.DESIGNATION.designation,
                "photo": image_url,
                "public_key": i.public_key,
            })

        return JsonResponse({"status": "ok", "data": soldier_list})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})



#===========================================================MAIN=======================================================
import os
import cv2
import base64
import numpy as np
from datetime import datetime
from PIL import Image
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
# --- UTILS ---

def binary_to_dna(binary_str):
    mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    if len(binary_str) % 2 != 0:
        binary_str += '0'
    dna = "".join(mapping.get(binary_str[i:i + 2], 'A') for i in range(0, len(binary_str), 2))
    return dna

def create_visual_shares(image_path, share1_dir, share2_dir):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("READ_ERROR: Image file not accessible.")

    h, w = img.shape
    share1 = np.random.randint(0, 256, (h, w), dtype=np.uint8)
    share2 = cv2.bitwise_xor(img, share1)

    base_name = os.path.basename(image_path)
    s1_name = f"share1_{base_name}"
    s2_name = f"share2_{base_name}"

    p1 = os.path.join(share1_dir, s1_name)
    p2 = os.path.join(share2_dir, s2_name)

    cv2.imwrite(p1, share1)
    cv2.imwrite(p2, share2)

    return p1, p2  # Returning FULL PATHS for immediate processing

def hide_message_in_image(image_path, dna_data, output_dir):
    # delimiter to find end of string during extraction
    dna_data += "###"
    binary_data = ''.join(format(ord(char), '08b') for char in dna_data)

    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size

    if len(binary_data) > width * height:
        raise ValueError("INSUFFICIENT_CAPACITY")

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_data):
                r, g, b = pixels[x, y]
                # LSB encoding on the Red channel
                new_r = (r & ~1) | int(binary_data[data_index])
                pixels[x, y] = (new_r, g, b)
                data_index += 1
            else:
                break
        if data_index >= len(binary_data): break

    save_name = f"steg_{os.path.splitext(os.path.basename(image_path))[0]}.png"
    full_path = os.path.join(output_dir, save_name)
    img.save(full_path, "PNG")

    # Return relative path for DB
    return os.path.join('share2', save_name)

# --- VIEWS ---

def process_upload_view_post(request):
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "POST_ONLY"}, status=405)

    try:
        if 'img' not in request.FILES:
            return JsonResponse({"status": "error", "message": "Primary carrier required."})

        uploaded_file = request.FILES['img']
        recipient_id = request.POST.get('reci_id')
        sender_lid = request.POST.get('lid')

        # Get dynamic coordinates from Flutter
        lat = request.POST.get('latitude', '0.0')
        lon = request.POST.get('longitude', '0.0')

        # 1. Payload Prep
        if 'img2' in request.FILES:
            secret_content = base64.b64encode(request.FILES['img2'].read()).decode('utf-8')
            prefix = "IMG:"
        elif 'msg' in request.POST:
            secret_content = request.POST['msg']
            prefix = "TXT:"
        else:
            return JsonResponse({"status": "error", "message": "No secret content provided."})

        # DNA Encoding
        full_payload = prefix + secret_content
        payload_bin = ''.join(format(ord(c), '08b') for c in full_payload)
        dna_encoded_data = binary_to_dna(payload_bin)

        # 2. Storage Setup
        fs = FileSystemStorage()
        fn = fs.save(uploaded_file.name, uploaded_file)
        original_path = fs.path(fn)

        s1_dir = os.path.join(settings.MEDIA_ROOT, 'share1')
        s2_dir = os.path.join(settings.MEDIA_ROOT, 'share2')
        os.makedirs(s1_dir, exist_ok=True)
        os.makedirs(s2_dir, exist_ok=True)

        # 3. Cryptography & Steganography
        p1, p2 = create_visual_shares(original_path, s1_dir, s2_dir)

        # Hide DNA data in Share 2
        steg_rel_path = hide_message_in_image(p2, dna_encoded_data, s2_dir)

        # 4. DB Operations
        sender = Soldier_table.objects.get(LOGIN=sender_lid)
        recipient = Soldier_table.objects.get(id=recipient_id)

        # Saving dynamic coordinates to the entry
        entry = data.objects.create(
            From_soldier=sender,
            To_soldier=recipient,
            data=fn,
            steg_data_path=steg_rel_path,
            date=datetime.now().date(),
            latitude=lat,
            longitude=lon,
        )

        return JsonResponse({
            "status": "ok",
            "message": "TRANSMISSION_SECURE",
            "steg_url": request.build_absolute_uri(settings.MEDIA_URL + steg_rel_path)
        })

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

def dna_encode_view(request):
    if request.method != 'POST': return JsonResponse({"status": "error", "message": "POST_ONLY"}, status=405)

    binary_input = request.POST.get('binary_str', '')
    if not binary_input or not all(b in '01' for b in binary_input):
        return JsonResponse({"status": "error", "message": "INVALID_BINARY_INPUT"}, status=400)

    dna_seq = binary_to_dna(binary_input)
    return JsonResponse({"status": "ok", "dna_sequence": dna_seq})


#===========================VIEW MSG=======================================

def view_shared_files(request):
    try:
        lid = request.POST['lid']
        user = Soldier_table.objects.get(LOGIN=lid)
        obj = data.objects.filter(To_soldier=user).order_by('-date')

        data_list = []
        for i in obj:
            # Build absolute URL for the steganographic image
            image_url = request.build_absolute_uri(settings.MEDIA_URL + str(i.data))

            data_list.append({
                "id": str(i.id),
                "from_name": i.From_soldier.soldier_name,
                "rank": i.From_soldier.DESIGNATION.designation,
                "date": str(i.date),
                "image": image_url,
                "latitude": str(i.latitude),
                "longitude": str(i.longitude),
            })

        return JsonResponse({"status": "ok", "data": data_list})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

# --- UTILITY FUNCTIONS --- 

def dna_to_binary(dna_str):
    mapping = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    return ''.join(mapping.get(char.upper(), '') for char in dna_str)

def binary_to_string(binary_str):
    chars = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i + 8]
        if len(byte) < 8:
            break
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def extract_dna_from_steg(steg_image_path):
    try:
        img = Image.open(steg_image_path).convert('RGB')
        pixels = np.array(img)

        red_channel = pixels[:, :, 0]
        flat_lsb = (red_channel & 1).flatten()

        extracted_chars = []
        for i in range(0, len(flat_lsb), 8):
            byte_bits = flat_lsb[i:i + 8]
            if len(byte_bits) < 8:
                break

            byte_val = 0
            for bit in byte_bits:
                byte_val = (byte_val << 1) | bit

            extracted_chars.append(chr(byte_val))

            if len(extracted_chars) >= 3:
                if "".join(extracted_chars[-3:]) == "###":
                    return "".join(extracted_chars)[:-3]
        return None
    except Exception as e:
        print(f"Extraction Error: {e}")
        return None

def combine_visual_shares(share1_path, share2_path):
    img1 = cv2.imread(share1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(share2_path, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        return None

    reconstructed = cv2.bitwise_xor(img1, img2)

    filename = "combined_" + os.path.basename(share1_path).replace("share1_", "")
    filename = os.path.splitext(filename)[0] + ".png"  # PNG is mandatory for lossless

    relative_dir = 'combined'
    full_dir = os.path.join(settings.MEDIA_ROOT, relative_dir)
    os.makedirs(full_dir, exist_ok=True)

    save_path = os.path.join(full_dir, filename)
    cv2.imwrite(save_path, reconstructed)

    return os.path.join(relative_dir, filename)

# --- VIEW FUNCTIONS (JSON RESPONSES) ---

def decrypt_message_api(request):
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "POST_ONLY"}, status=405)

    data_id = request.POST.get('data_id')
    if not data_id:
        return JsonResponse({"status": "error", "message": "MISSING_DATA_ID"})

    try:
        data_obj = get_object_or_404(data, id=data_id)

        # 1. Locate File Paths
        original_filename = str(data_obj.data)
        share1_filename = f"share1_{original_filename}"

        share1_path = os.path.join(settings.MEDIA_ROOT, 'share1', share1_filename)
        steg_share2_path = os.path.join(settings.MEDIA_ROOT, data_obj.steg_data_path)

        if not os.path.exists(share1_path) or not os.path.exists(steg_share2_path):
            return JsonResponse({"status": "error", "message": "SHARES_NOT_FOUND_ON_SERVER"})

        # 2. Steganography Extraction
        extracted_dna = extract_dna_from_steg(steg_share2_path)
        if not extracted_dna:
            return JsonResponse({"status": "error", "message": "DNA_DECODING_FAILED"})

        # 3. Decoding Pipeline
        hidden_binary = dna_to_binary(extracted_dna)
        full_payload = binary_to_string(hidden_binary)

        # 4. Visual Reconstruction
        combined_rel_path = combine_visual_shares(share1_path, steg_share2_path)
        reconstructed_url = request.build_absolute_uri(settings.MEDIA_URL + combined_rel_path)

        # 5. Determine Payload Type
        is_image = False
        hidden_text = ""
        hidden_image_base64 = ""

        if full_payload.startswith("IMG:"):
            is_image = True
            hidden_image_base64 = full_payload.replace("IMG:", "")
        elif full_payload.startswith("TXT:"):
            hidden_text = full_payload.replace("TXT:", "")
        else:
            hidden_text = full_payload  # Generic fallback

        return JsonResponse({
            "status": "ok",
            "message": "DECRYPTION_SUCCESSFUL",
            "data": {
                "reconstructed_image_url": reconstructed_url,
                "is_image": is_image,
                "hidden_text": hidden_text,
                "hidden_image_base64": hidden_image_base64,
                "metadata": {
                    "payload_length": len(full_payload),
                    "dna_sequence": extracted_dna[:15] + "..."
                }
            }
        })

    except Exception as e:
        return JsonResponse({"status": "error", "message": f"CRITICAL_FAULT: {str(e)}"}, status=500)


def dna_to_binary_view(request):
    if request.method != 'POST': return JsonResponse({"status": "error"}, status=405)
    dna_input = request.POST.get('dna_str', '')
    if not dna_input: return JsonResponse({"status": "error", "message": "dna_str required"})

    return JsonResponse({
        "status": "ok",
        "binary_data": dna_to_binary(dna_input)
    })


def binary_to_string_view(request):
    if request.method != 'POST': return JsonResponse({"status": "error"}, status=405)
    binary_input = request.POST.get('binary_str', '')
    if not binary_input: return JsonResponse({"status": "error", "message": "binary_str required"})

    decoded = binary_to_string(binary_input)
    return JsonResponse({
        "status": "ok",
        "payload": decoded,
        "type": "IMAGE" if decoded.startswith("IMG:") else "TEXT"
    })