#ifndef _MAYBE_H_
#define _MAYBE_H_

#include <exception>

namespace maybe {
struct UnwrapNone : std::exception {
  const char* what() const throw() { return "Unwrapped None value"; }
};

template <typename T, typename V>
using MapFn = V (*)(T);
template <typename T>
using ThenFn = void (*)(T);

template <typename T>
class Maybe {
 protected:
  T _value;
  bool _some;

 public:
  Maybe(T value) : _value(value), _some(true) {};
	Maybe() : _some(false) {};
  bool is_some() { return this->_some; }
  bool is_none() { return !this->_some; }
  T unwrap() {
    if (!this->_some) throw maybe::UnwrapNone();
    return this->_value;
  }
  T unwrap_or(T value) {
    if (this->_some)
      return this->_value;
    else
      return value;
  }
  template <typename V>
  Maybe<V> map(MapFn<T, V> map_fn) {
    if (this->_some)
      return maybe::Maybe<V>(map_fn(this->_value));
    else
      return maybe::Maybe<V>();
  }
  Maybe<T> then(ThenFn<T> then_fn) {
    if (this->_some) then_fn(this->_value);
    return *this;
  }
};

template <typename T>
Maybe<T> some(T value) {
  return Maybe<T>(value);
}
template <typename T>
Maybe<T> none() {
  return Maybe<T>();
}
}  // namespace maybe

#endif  //_MAYBE_H_
