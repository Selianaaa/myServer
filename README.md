# myServer

# Project Title

HTTP-server handle requests

# Requirements

* Python
* Django
* Docker

# Getting Started

Make migrations

    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate

Up server

    Docker-compose up

#Example

To create item make HTTP request to 'http://localhost:8000/items/create' (method: POST), response body would be

    {
      "msg": "OK",
      "id": "3ae9e120-cd14-436e-9790-93b5566b29c4"
    }

To add image vector make HTTP request to 'http://localhost:8000/items/3ae9e120-cd14-436e-9790-93b5566b29c4/add_vector' (method: POST + image file), response body would be

    'Success' if image vector created

To get more item info make HTTP request to 'http://localhost:8000/items/3ae9e120-cd14-436e-9790-93b5566b29c4/information' (method: GET), response body would be

    {
      "id": "3ae9e120-cd14-436e-9790-93b5566b29c4",
      "created": "2019-09-13T20:12:19.540Z",
      "hasVector": "yes"
    }

To see all existin items make HTTP request to 'http://localhost:8000/items/show' (method: GET), response body would be

      {
        "ids":[
          "26451dfb-413e-4825-8e51-64d9adc9461b",
          "3ae9e120-cd14-436e-9790-93b5566b29c4"
        ]
      }

To download item image make HTTP request to 'http://localhost:8000/items/3ae9e120-cd14-436e-9790-93b5566b29c4/download_image' (method: GET), response body would be grey image

To delete item make HTTP request to 'http://localhost:8000/items/3ae9e120-cd14-436e-9790-93b5566b29c4/remove' (method: DELETE), response body would be

      'OK' if image deleted
