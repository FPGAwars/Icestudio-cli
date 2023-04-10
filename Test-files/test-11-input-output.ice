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
          "id": "0766f96f-9f07-49b1-8c78-f24dce15cb5e",
          "type": "basic.input",
          "data": {
            "name": "Btn",
            "virtual": false,
            "range": "[1:0]",
            "pins": [
              {
                "index": "1",
                "name": "SW2",
                "value": "33"
              },
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
            "y": -120
          }
        },
        {
          "id": "f2c3641d-ddfd-4a4b-a092-33b6f4bf838a",
          "type": "basic.output",
          "data": {
            "name": "LED",
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
                "name": "LED0",
                "value": "45"
              }
            ]
          },
          "position": {
            "x": 288,
            "y": -120
          }
        }
      ],
      "wires": [
        {
          "source": {
            "block": "0766f96f-9f07-49b1-8c78-f24dce15cb5e",
            "port": "out"
          },
          "target": {
            "block": "f2c3641d-ddfd-4a4b-a092-33b6f4bf838a",
            "port": "in"
          },
          "size": 2
        }
      ]
    }
  },
  "dependencies": {}
}