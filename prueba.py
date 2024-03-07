import facebook

# Token de acceso a la API de Facebook
ACCESS_TOKEN = 'EAAEgJ5L1NjEBO2bdFK2Hyef8tnQSCOq5D8ZASH6AAPKjxzbqeqsbZBs6fsyIyq7L0HcbztKmefkTHPjSJZAO0l2LTa9fDgLr5L8rzIFcRsK4ctJnSQqF6hyJDZC0kO4Vf1dZCOvdPhdfprKeN2RrRgREzGZAMqDtZBYFIKzwzCEtKlGuQ1a67xzKsUF3QZDZD'

# ID de la página de Facebook que deseas consultar
pagina_id = '173751902760964'

# Crear una instancia de la API de Facebook
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)

# Obtener información sobre la página
info_pagina = graph.get_object(id=pagina_id)

# Imprimir información sobre la página
print("Nombre de la página:", info_pagina['name'])
print("Categoría de la página:", info_pagina['category'])
print("Descripción de la página:", info_pagina.get('description', 'No disponible'))
print("Número de seguidores:", info_pagina['fan_count'])
