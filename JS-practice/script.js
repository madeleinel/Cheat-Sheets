// -------- from JS30 Array Cardio I -------- //

// // arrow functions           // //
// // the base constants        // //
// // .filter                   // // ...all of these functions will automatically loop through all objects within the array
// // .map                      // //
// // .sort                     // //
// // .reduce                   // //
// // concatenating functions   // //

// ---- ARROW FUNCTIONS ---- //

// // both below mean the same thing:
// // dogs.sort(function(a, b) {});
// // dogs.sort((a, b) => {});

// ---- THE BASE CONSTANTS ---- //

// const containing OBJECTS; each object represents a dog
const dogs = [
  {name: 'Fido', type: 'labrador', age: 3, born: 2014},
  {name: 'Spot', type: 'golden retreiver', age: 4, born: 2013},
  {name: 'Caspar', type: 'chihuahua', age: 3, born: 2014},
  {name: 'Betsy', type: 'dalmatian', age: 1, born: 2016}
];

// an ARRAY containing the names of different cats
const cats = [
  'Black Betty', 'Orange Tabby', 'Grey Whiskers', 'Brown George'
];

const currentYear = 2017;

const vehicles = ['car', 'boat', 'car', 'truck', 'lorry', 'bus', 'boat', 'bus', 'car', 'motorcycle', 'car'];

// ---- .FILTER ---- //

// create a variable containing all dogs aged 2 or older
// use .FILTER and pass it a function, to make that function loop over all objects within the 'dogs' const, and return the objects that fit the function's criteria
// set the filter function to loop through the 'dogs' constant >> ask it to return the object IF the object's age (dogs.age) is >= 2
const nonPuppies = dogs.filter(function(dogs) {
  if(dogs.age >= 2) {
    return true; // ie if the dogs age is >= 2 >> keep it / include it within the 'nonPuppies' constant
  } // no need to return FALSE for object's that don't fulfill this criteria >> these will be discarded anyways
});

// it can also be rewritten as an ARROW FUNCTION & shorten the if/else statement to an inline statement which only return the specified objects
const adultDogs = dogs.filter(dogs => // arrow function
  dogs.age >= 2) // telling the function to return only these objects

//// nonPuppies and adultDogs will return the same data
// to return the relevant objects within a table
// console.table(nonPuppies);
// console.table(adultDogs);

// ---- .MAP ---- //

// create an array of the dogs' name and type
// use .MAP and pass it a function, to make that function loop through the array & then return a new array containing the requested data (will be of the same length as the orginal array [whereas .filter can return a dataset of a different length than the original])
const dogID = dogs.map(dogs => // ARROW FUNCTION
  dogs.name + ' ' + dogs.type) // tell the function to return each dog's name (dogs.name) and type (dogs.type)
                                // returns 'var + space + var' by concatenating a BLANK SPACE between the variables

const doggieID = dogs.map(dogs =>
  `${dogs.name} ${dogs.type}`) // can also make it return 'var + space + var' by using TEMPLATE STRINGS

// return the new arrays containing the dog ID's
// console.log(dogID);
// console.log(doggieID);

// ---- .SORT ---- //

// sort the dogs by their ages
// use .SORT and pass it a function
// give the function 2 items (firstAge and secondAge) and ask it to compare them
// returning 1 if the first dog is older than the comparison makes it move up the table, and returning -1 if it's younger than the comparison makes it move down the table
const dogAges = dogs.sort(function(firstAge, secondAge) { // or function(a, b)
  if(firstAge.age > secondAge.age) {
    return 1;
  } else {
    return -1;
  }
});

// can also shorten this function down by using an ARROW FUNCTION and a TURNIRARY OPERATOR
const agesOrdered = dogs.sort((a, b) => // ARROW FUNCTION
  // TURNIRARY OPERATOR: (can all be written on one line)
  a.age > b.year // check whether this condition is met
  ? 1 // '?' = if 'a.year > b.year'is true then do the following ('add 1')
  : -1 ) // ':' = 'otherwise do the following' >> so if 'a.year !> b.year', return -1

// return a table consisting of all objects within the constant 'dogs', sorted by their ages
// console.table(dogAges);
// console.table(agesOrdered);

// ----------------

// sort the dogs based on their age, calculating their age based on their birth year & the current year
const oldestDog = dogs.sort(function(a, b) {
  const lastDog = currentYear - a.born;
  const nextDog = currentYear - b.born;

  if(lastDog > nextDog) {
    return -1;
  } else {
    return 1;
  }
});

// can also shorten the if/else statement
const oldestDoggie = dogs.sort((a, b) => {
  const lastDog = currentYear - a.born;
  const nextDog = currentYear - b.born;

  return lastDog > nextDog ? -1 : 1;  // shorten the if/else statement
});

// console.table(oldestDog);
// console.table(oldestDoggie);

// ----------------

// .SPLITting strings
const splitCats = cats.sort(function(lastCat, nextCat) {
  const parts = lastCat.split(' ')  // define where to split each string >> ie, at the ' ' between the words
  // console.log(parts);    >> will return an array for each cat, containing two strings >> the strings will not include the ' ' that the original string was split around
  // >> whereas 'console.log(lastCat)' will return a string for each cat

  // to change the order of the words and return that as a new string
  const [colour, type] = lastCat.split(' '); // define that the string should be split into the variables 'colour' and 'type'
  // console.log(type, colour); // define which order to display the variables in (as usual)
                             // using ', ' instead of '+' will print the two words with a space between them
  // 'parts' = array
  // 'colour' & 'type' = constants
});

// sort the cats alphabetically by their type
// 'cats' = an ARRAY
// .SPLIT to split each string within the array
const alpha = cats.sort((lastCat, nextCat) => {
  const [aColour, aType] = lastCat.split(' '); // split 'lastCat' into constants 'colour' and 'type'
  const [bColour, bType] = nextCat.split(' '); // split 'nextCat' into constants 'colour' and 'type'

  // set up shortened if/else statement to sort alphabetically based on the cat type
  return aType > bType ? 1 : -1;
});

// console.log(alpha);
// alpha is still 'holding onto the original strings we were working with' (ie "colour type") >> we are only using the new constants 'name' and 'type' for the conversion / to sort the strings based on those variables
// >> if want to return an ARRAY or OBJECT instead >> use .REDUCE

// ---- .REDUCE ---- //

// calculate the combined age of all dogs together
// can use .REDUCE instead of a long FOR LOOP
// will 'return what the running tally is / what was returned last time'
const totalAge = dogs.reduce((total, dogs) => {
  return total + (dogs.age);// total = 'what the total was last time around'
}, 0); // Need to set 'total' to 0, otherwise it will be 'undefined' the first time the function runs (as nothing has been added to it yet at that point)

// console.log(totalAge);

// console.log(currentYear);
// console.log(dogs[1].born);
// console.log(currentYear-dogs[1].born);

// ----------------

// sum up the instances of each vehicle type within the const 'vehicles'
// using .REDUCE >> start with a blank object >> the create & increase items within the object
const transportation = vehicles.reduce((object, item) => {  // 'item' = each individual string within the array >> eg 'car', 'boat'
  if(!object[item]) {
    object[item] = 0;  // if the current item has not been defined as '0' at the end of the function (ie 'car:0, etc') >> create it and define it (the inital value of it) as '0'
  }

  object[item]++;  // set the count for each vehicle type to increase by 1 each time it is encountered within the array

  return object;
}, {}   // create an emply object >> instead of setting 'car:0, boat:0, etc' >> see line 170-172
);

// print the object containing all item names and the number of times they occur within the object
console.log(transportation);

// ---- CONCATENATING FUNCTIONS ---- //

// To test it >> type this is the Dev Tools Console on https://en.wikipedia.org/wiki/Category:Boulevards_in_Paris

// Retreive all boulevard names containing 'de' from https://en.wikipedia.org/wiki/Category:Boulevards_in_Paris
// Get the DOM elements from the page
// within the Dev Tools Elements on the page >> find which elements contain the boulevard names
// then create a variable calling on that element
const category = document.querySelector('.mw-category'); // find an element within the page
const links = Array.from(category.querySelectorAll('a')); // find an element within the '.mw-category' element

// to do this in one line:
// const categoryLinks = document.querySelector('.mw-category a');

// // note >> using .querySelectorAll will return a node list >> can't use .map with that (only forEach etc)
// // instead, need to change const 'links' into an array >> within const 'links', need to use either
// // // a) Array.from(category.querySelectorAll('a'));   >> 'Array.from' converts it into an array
// // // b) [...category.querySelectorAll('a')];   >> '[]' to create an array & '...' to spread the items within the array

// sort through all the links and only return the ones containing 'de'
const allBoulevards = links.map(link => // map over / go through all objects within the list of links
  link.textContent); // return the text within each link >> ie the value of link.textContent

// return an array containing all boulevard names containing 'de'
const de = links
    .map(link => link.textContent)  // return the text within all links
    .filter(streetName => streetName.includes('de')); // filter through all of these and only return the ones containing 'de'

// // note >> can put all of these on the same line
// // ie:
// // const de = links.map(link => link.textContent).filter(streetName => streetName.includes('de'));
