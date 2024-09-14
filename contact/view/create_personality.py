from contact.google_ai_api.cliente import get_contact_description


def contact_pre_save(contact):

    if contact.description:
        personality = get_contact_description(
            contact.description, contact.category)
        contact.personality = personality
        print('Personalidade cadastrada')
