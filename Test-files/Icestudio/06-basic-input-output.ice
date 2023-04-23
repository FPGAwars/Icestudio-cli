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
          "id": "ffe0daa9-1e54-4085-b544-89c5d9a41626",
          "type": "basic.input",
          "data": {
            "name": "i0",
            "virtual": false,
            "pins": [
              {
                "index": "0",
                "name": "SW1",
                "value": "34"
              }
            ],
            "clock": false
          },
          "position": {
            "x": -440,
            "y": -16
          }
        },
        {
          "id": "a946697d-809f-4a70-95f4-1697e2829f6b",
          "type": "basic.output",
          "data": {
            "name": "o0",
            "virtual": false,
            "pins": [
              {
                "index": "0",
                "name": "LED0",
                "value": "45"
              }
            ]
          },
          "position": {
            "x": -168,
            "y": -16
          }
        },
        {
          "id": "6e4647a8-bec0-490e-96c2-b215345b630f",
          "type": "basic.output",
          "data": {
            "name": "o0",
            "virtual": false,
            "range": "[1:0]",
            "pins": [
              {
                "index": "1",
                "name": "LED1",
                "value": "44"
              },
              {
                "index": "0",
                "name": "LED2",
                "value": "43"
              }
            ]
          },
          "position": {
            "x": -168,
            "y": 112
          }
        },
        {
          "id": "45d4e511-e598-48c1-bcec-5b4c29f36c5b",
          "type": "basic.input",
          "data": {
            "name": "Input",
            "virtual": false,
            "range": "[1:0]",
            "pins": [
              {
                "index": "1",
                "name": "D0",
                "value": "2"
              },
              {
                "index": "0",
                "name": "D1",
                "value": "1"
              }
            ],
            "clock": false
          },
          "position": {
            "x": -440,
            "y": 120
          }
        }
      ],
      "wires": []
    }
  },
  "dependencies": {}
}