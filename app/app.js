const apiKey = "f897a99d971b5eef57be6fafa0d83239";

export default async function getGeoLoc(input) {
    let path = "";
    const query = encodeURI(`${input},US`);
    if(isNaN(input)){
        path = `direct?q=${query}&limit=5&appid=${apiKey}`;
    }
    else{
        path = `zip?zip=${query}&limit=5&appid=${apiKey}`;
    }
    
    const url = `https://api.openweathermap.org/geo/1.0/${path}`;
    const response = await fetch(url);

    // console.log(`response: ${response}`)

    let location = await response.json();
    if(Array.isArray(location) && location.length > 0)
        location = location[0];

    const result = {};

    if("name" in location){
        result.name = location.name;
        result.lat = location.lat;
        result.long = location.lon
    }

    return new Promise((resolve, reject) => {
        resolve(result);
    });
}

async function getGeoLocations(inputs){
    let results = [];
    for(const i in inputs){
        const result = await getGeoLoc(inputs[i]);
        results.push(result);
    }
    return results;
}

const args = process.argv.slice(2, process.argv.length);

getGeoLocations(args).then(results => {
    console.log(results);
})