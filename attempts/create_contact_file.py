#create a function that creates a .vcf file
#input: name, phone number, email
#output: .vcf file
def make_vcard(
        first_name,
        last_name,
        company,
        title,
        phone,
        address,
        email):
    address_formatted = ';'.join([p.strip() for p in address.split(',')])
    return [
        'BEGIN:VCARD',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'ADR;WORK;PREF:;;{address_formatted}',
        f'REV:1',
        'END:VCARD'
    ]

def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])

if __name__ =="__main__":
    #create_contact_file()
    vcf_file = f'{"stathopoulos".lower()}.vcf'
    vcard = make_vcard("stathopoulos", "stavros", "UPatras", "Prof", "1234567890", "Patras", "sstath@upatras.gr")
    write_vcard(vcf_file, vcard)
