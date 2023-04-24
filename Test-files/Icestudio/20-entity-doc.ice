{
  "version": "1.2",
  "package": {
    "name": "",
    "version": "",
    "description": "",
    "author": "",
    "image": ""
  },
  "design": {
    "board": "alhambra-ii",
    "graph": {
      "blocks": [
        {
          "id": "70e477be-9fc9-4fe7-a307-ddc393f3826f",
          "type": "dd781bbf9b1e50824851efd3fbf39bb85daa31b0",
          "position": {
            "x": -624,
            "y": -416
          },
          "size": {
            "width": 96,
            "height": 64
          }
        }
      ],
      "wires": []
    }
  },
  "dependencies": {
    "dd781bbf9b1e50824851efd3fbf39bb85daa31b0": {
      "package": {
        "name": "Generic-DOC",
        "version": "0.1",
        "description": "Bloque con documentación",
        "author": "Juan González-Gómez",
        "image": "%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20465.46%20465.46%22%3E%3Cpath%20fill=%22#e2b369%22%20d=%22M406.995%2078.76v377.7h-278.76v-25.89h252.88V78.76z%22/%3E%3Cpath%20fill=%22#e2b369%22%20d=%22M372.115%2043.88v377.69H93.355v-25.88h252.88V43.88zM127.805%2015.36v62.97h-62.97z%22/%3E%3Cpath%20d=%22M337.235%209v377.69H58.465V87.33h78.34V9h200.43zm-42.92%20333.82v-9h-192.93v9h192.93zm0-37.4v-9h-192.93v9h192.93zm0-37.4v-9h-192.93v9h192.93zm0-37.39v-9h-192.93v9h192.93zm0-37.4v-9h-192.93v9h192.93zm0-37.4v-9h-192.93v9h192.93zm0-37.4v-9h-192.93v9h192.93zm-47.64-37.4v-9h-92.01v9h92.01z%22%20fill=%22#ffcc73%22/%3E%3Cpath%20d=%22M415.995%2069.76v395.7h-296.76v-34.89h-34.88v-34.88h-34.89V80.97L130.445%200h215.79v34.88h34.88v34.88h34.88zm-9%20386.7V78.76h-25.88v351.81h-252.88v25.89h278.76zm-34.88-34.89V43.88h-25.88v351.81H93.355v25.88h278.76zm-34.88-34.88V9h-200.43v78.33h-78.34v299.36h278.77zM127.805%2078.33V15.36l-62.97%2062.97h62.97z%22/%3E%3Cpath%20d=%22M101.385%20333.82h192.93v9h-192.93zM101.385%20296.42h192.93v9h-192.93zM101.385%20259.02h192.93v9h-192.93zM101.385%20221.63h192.93v9h-192.93zM101.385%20184.23h192.93v9h-192.93zM101.385%20146.83h192.93v9h-192.93zM101.385%20109.43h192.93v9h-192.93zM154.665%2072.03h92.01v9h-92.01z%22/%3E%3C/svg%3E",
        "otid": 1682322071547
      },
      "design": {
        "graph": {
          "blocks": [
            {
              "id": "42a6bba6-0c2c-49d0-9fa5-1fc9ab26f8c9",
              "type": "basic.info",
              "data": {
                "info": "My doc!",
                "readonly": true
              },
              "position": {
                "x": 432,
                "y": 208
              },
              "size": {
                "width": 248,
                "height": 56
              }
            }
          ],
          "wires": []
        }
      }
    }
  }
}