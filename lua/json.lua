local cjson = require("cjson")

local obj = {
    id = 1,
    name = "zhan",
    age = nil,
    is_male = false,  
    hobby = {"film", "music", "read"} 
}
local s = cjson.encode(obj)
print(s, "<br/>")
