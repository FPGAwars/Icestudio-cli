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
          "id": "ee908964-98bc-4079-9383-0de7991be814",
          "type": "basic.code",
          "data": {
            "ports": {
              "in": [
                {
                  "name": "i0"
                },
                {
                  "name": "i1",
                  "range": "[1:0]",
                  "size": 2
                },
                {
                  "name": "i2",
                  "range": "[7:0]",
                  "size": 8
                }
              ],
              "out": [
                {
                  "name": "o0"
                },
                {
                  "name": "o1",
                  "range": "[1:0]",
                  "size": 2
                },
                {
                  "name": "o2",
                  "range": "[7:0]",
                  "size": 8
                }
              ]
            },
            "params": [
              {
                "name": "P"
              },
              {
                "name": "N"
              }
            ],
            "code": "//-- Hi!"
          },
          "position": {
            "x": -696,
            "y": -456
          },
          "size": {
            "width": 192,
            "height": 128
          }
        }
      ],
      "wires": []
    }
  },
  "dependencies": {}
}