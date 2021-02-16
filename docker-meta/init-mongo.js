db.createUser({
    user: 'root',
    pwd: 'toor',
    roles: [
        {
            role: 'readWrite',
            db: 'testDB',
        },
    ],
})

db = new Mongo().getDB("testDB")

db.createCollection('images', { capped: false })
db.createCollection('passthru', { capped: false })

db.images.insert([
  {
    "image" : "baiduxlab/sgx-rust" ,
    "platform" : {
      "cpu" : {
        "architecture" : "amd64" ,
        "features" : {
          "SGX" : "required"
        }
      },
      "hardware" : {},
      "os" : "linux"
    }}
  ])

  db.passthru.insert([
    {
    "platform" : "SGX",
    "passthru−devices" : ["/dev/isgx" , "/dev/mei0"],
    }
    ])
