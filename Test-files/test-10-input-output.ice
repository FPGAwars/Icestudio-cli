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
          "id": "d808af95-83d8-4702-a00c-2f00e8856c02",
          "type": "basic.input",
          "data": {
            "name": "Boton",
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
            "x": 96,
            "y": -104
          }
        },
        {
          "id": "e63744e7-23e0-474e-90b6-830f0cf82e9c",
          "type": "basic.output",
          "data": {
            "name": "LED",
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
            "x": 288,
            "y": -104
          }
        }
      ],
      "wires": [
        {
          "source": {
            "block": "d808af95-83d8-4702-a00c-2f00e8856c02",
            "port": "out"
          },
          "target": {
            "block": "e63744e7-23e0-474e-90b6-830f0cf82e9c",
            "port": "in"
          }
        }
      ]
    }
  },
  "dependencies": {}
}