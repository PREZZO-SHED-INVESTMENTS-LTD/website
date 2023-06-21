const production = true



export let url : string
export let mediaurl : string
export let internalURL : string
if(!production){
     url = 'http://41.242.51.98:443/'
     mediaurl ='http://41.242.51.98:443'

}


if(production){
    url = 'http://41.242.51.98:443/'
    mediaurl='http://41.242.51.98:443'

}
