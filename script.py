import os

# Ensure the directory exists
output_dir = 'typescript_files'
os.makedirs(output_dir, exist_ok=True)

# List of TypeScript code snippets to populate the files
typescript_snippets = [
    # Add your TypeScript snippets here
    'let message: string = "Hello, TypeScript!";',
    'function add(a: number, b: number): number { return a + b; }',
    'class Person { constructor(public name: string, public age: number) {} }',
    'interface User { id: number; name: string; }',
    'enum Direction { Up, Down, Left, Right }',
    'type StringOrNumber = string | number;',
    'const names: string[] = ["Alice", "Bob", "Charlie"];',
    'let tuple: [string, number]; tuple = ["hello", 10];',
    'function identity<T>(arg: T): T { return arg; }',
    'class GenericNumber<T> { zeroValue: T; add: (x: T, y: T) => T; }',
    'let myAdd: (x: number, y: number) => number = function(x, y) { return x + y; };',
    'namespace Validation { export interface StringValidator { isAcceptable(s: string): boolean; } }',
    'abstract class Animal { abstract makeSound(): void; move(): void { console.log("roaming the earth..."); } }',
    'interface Point { x: number; y: number; }',
    'function logPoint(p: Point) { console.log(`${p.x}, ${p.y}`); }',
    'class Greeter { greeting: string; constructor(message: string) { this.greeting = message; } greet() { return `Hello, ${this.greeting}`; } }',
    'interface LabelledValue { label: string; } function printLabel(labelledObj: LabelledValue) { console.log(labelledObj.label); }',
    'function createSquare(config: {color?: string; width?: number;}) { let newSquare = {color: "white", area: 100}; if (config.color) { newSquare.color = config.color; } if (config.width) { newSquare.area = config.width * config.width; } return newSquare; }',
    'let list: number[] = [1, 2, 3];',
    'class Car { private engine: string; constructor(engine: string) { this.engine = engine; } start() { console.log(`Engine started: ${this.engine}`); } }',
    'function padLeft(value: string, padding: string | number) { if (typeof padding === "number") { return Array(padding + 1).join(" ") + value; } if (typeof padding === "string") { return padding + value; } throw new Error(`Expected string or number, got ${typeof padding}.`); }',
    'interface SquareConfig { color?: string; width?: number; } function createSquare(config: SquareConfig): {color: string; area: number} { let newSquare = {color: "white", area: 100}; if (config.color) { newSquare.color = config.color; } if (config.width) { newSquare.area = config.width * config.width; } return newSquare; }',
    'function extend<T, U>(first: T, second: U): T & U { let result = {} as T & U; for (let id in first) { (result as any)[id] = (first as any)[id]; } for (let id in second) { if (!result.hasOwnProperty(id)) { (result as any)[id] = (second as any)[id]; } } return result; }',
    'function pluck<T, K extends keyof T>(o: T, names: K[]): T[K][] { return names.map(n => o[n]); }',
    'interface Bird { fly(): void; layEggs(): void; } interface Fish { swim(): void; layEggs(): void; } function getSmallPet(): Fish | Bird { return Math.random() > 0.5 ? { fly() {}, layEggs() {} } : { swim() {}, layEggs() {} }; }',
    'function isNumber(x: any): x is number { return typeof x === "number"; } function isString(x: any): x is string { return typeof x === "string"; }',
    'class Control { private state: any; } interface SelectableControl extends Control { select(): void; } class Button extends Control implements SelectableControl { select() {} }',
    'interface Counter { (start: number): string; interval: number; reset(): void; } function getCounter(): Counter { let counter = <Counter>function (start: number) {}; counter.interval = 123; counter.reset = function () {}; return counter; }',
    'function sealed(constructor: Function) { Object.seal(constructor); Object.seal(constructor.prototype); }',
    'function f(input: boolean) { let a = 100; if (input) { let b = a + 1; return b; } return a; }',
    'let sym1 = Symbol(); let sym2 = Symbol("key");',
    'function* fib(): IterableIterator<number> { let a = 0, b = 1; while (true) { yield a; [a, b] = [b, a + b]; } }',
    'type LinkedList<T> = T & { next: LinkedList<T> };',
    'type Alias = { num: number }; interface Interface { num: number; }',
    'class C { private _length = 0; get length() { return this._length; } set length(value) { this._length = value; } }',
    'class Octopus { readonly numberOfLegs: number = 8; constructor(readonly name: string) {} }',
    'class Grid { static origin = {x: 0, y: 0}; calculateDistanceFromOrigin(point: {x: number; y: number}) { let xDist = (point.x - Grid.origin.x); let yDist = (point.y - Grid.origin.y); return Math.sqrt(xDist * xDist + yDist * yDist) / this.scale; } constructor (public scale: number) {} }',
    'interface Square { kind: "square"; size: number; } interface Rectangle { kind: "rectangle"; width: number; height: number; } interface Circle { kind: "circle"; radius: number; } type Shape = Square | Rectangle | Circle;',
    'function area(s: Shape) { switch (s.kind) { case "square": return s.size * s.size; case "rectangle": return s.height * s.width; case "circle": return Math.PI * s.radius ** 2; } }',
    'function error(message: string): never { throw new Error(message); }',
    'let suits = ["hearts", "spades", "clubs", "diamonds"]; function pickCard(x: {suit: string; card: number; }[]): number; function pickCard(x: number): {suit: string; card: number; }; function pickCard(x: any): any { if (typeof x == "object") { let pickedCard = Math.floor(Math.random() * x.length); return pickedCard; } else if (typeof x == "number") { let pickedSuit = Math.floor(x / 13); return { suit: suits[pickedSuit], card: x % 13 }; } }',
    'class BeeKeeper { hasMask: boolean; } class ZooKeeper { nametag: string; } class Animal { numLegs: number; } class Bee extends Animal { keeper: BeeKeeper; } class Lion extends Animal { keeper: ZooKeeper; } function createInstance<A extends Animal>(c: new () => A): A { return new c(); }',
    'type EventNames = "click" | "scroll" | "mousemove"; function handleEvent(ele: Element, event: EventNames) { /* ... */ }',
    'class Component { protected element: HTMLElement; constructor(element: HTMLElement) { this.element = element; } } class SubComponent extends Component { private someProperty: string; constructor(element: HTMLElement, someProperty: string) { super(element); this.someProperty = someProperty; } }'
]

# Ensure we have at least 50 snippets
while len(typescript_snippets) < 50:
    typescript_snippets.extend(typescript_snippets)

# Write the TypeScript snippets to files
for i in range(50):
    filename = os.path.join(output_dir, f'typescript_file_{i + 1}.ts')
    with open(filename, 'w') as file:
        file.write(typescript_snippets[i])

print(f"Created 50 TypeScript files in '{output_dir}' directory.")
