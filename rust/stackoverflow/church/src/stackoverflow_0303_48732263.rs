// @filename   : stackoverflow_0303_48732263.rs
// @date       : Wed Nov 16 12:31:09 PM HKT 2022
// @author     : Church.ZHONG
// @see        : https://stackoverflow.com/questions/48732263
// @title      : Why is Rust's assert_eq! implemented using a match?

#[allow(dead_code)]
mod answer1 {

    /*
    Indeed, match expr { x => {...} } is the Rust equivalent of let x = expr in ..., in that it's the most relaxed with respect to lifetime temporaries and "should always work",
    e.g. match e { x => f(x) } should be always equivalent to f(e).
    On the other hand, let x = expr; is more "imperative" and doesn't allow keeping nested temporaries around,
    e.g. let x = f(&g()); only compiles if f uses its reference argument without returning it, as the temporary it points to only lives for the duration of the call.
    */

    mod code1 {
        pub fn test() {
            // add your code here
        }
    }
    mod code2 {
        pub fn test() {
            // add your code here
        }
    }
    mod code3 {
        pub fn test() {
            // add your code here
        }
    }
    pub fn test() {
        //code1::test();
        //code2::test();
        //code3::test();
    }
}
#[allow(dead_code)]
mod answer2 {
    mod code1 {
        pub fn test() {
            // add your code here
        }
    }
    mod code2 {
        pub fn test() {
            // add your code here
        }
    }
    mod code3 {
        pub fn test() {
            // add your code here
        }
    }
    pub fn test() {
        //code1::test();
        //code2::test();
        //code3::test();
    }
}
#[allow(dead_code)]
mod answer3 {
    mod code1 {
        pub fn test() {
            // add your code here
        }
    }
    mod code2 {
        pub fn test() {
            // add your code here
        }
    }
    mod code3 {
        pub fn test() {
            // add your code here
        }
    }
    pub fn test() {
        //code1::test();
        //code2::test();
        //code3::test();
    }
}
pub fn test() {
    _enter!();
    //answer1::test();
    //answer2::test();
    //answer3::test();
    _leave!();
}
