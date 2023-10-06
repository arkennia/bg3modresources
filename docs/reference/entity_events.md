```lua
Ext.Osiris.RegisterListener("EntityEvent", 2, "after", function(guid, id)
    if id == "AS_bagItems_OnItem" then
        BasicDebug("EVENT - EntityEvent Inventory Iteration for event : " .. id)
        REMOVER_BAG_CONTENT_LIST[GetItemName(guid)] = string.sub(Osi.GetTemplate(guid), -36)

end)
```

let's say you did your MoveItemTo and gave it the AS_bagItems_OnItem string for the event parameter
you can listen to EntityEvent for the given event
and do something else
