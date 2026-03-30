# Domain model for RoomLight

Controller  
├── Room (1..n)  
│ └── LightBulb (1..n)  
├── LightPreset (0..n)  
├── RoomPreset (0..n)  
└── Alert (0..n)

RoomPreset  
└── LightPreset (1..n)  
└── applies to → Room / LightBulb

Alert  
└── relates to → LightBulb
