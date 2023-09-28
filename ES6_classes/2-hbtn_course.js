/* eslint-disable class-methods-use-this */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateString(name, 'Name');
    this._length = this._validateNumber(length, 'Length');
    this._students = this._validateArray(students, 'Students');
  }

  get name() {
    return this._name;
  }

  set name(name) {
    this._name = this._validateString(name, 'Name');
  }

  get length() {
    return this._length;
  }

  set length(length) {
    this._length = this._validateNumber(length, 'Length');
  }

  get students() {
    return this._students;
  }

  set students(students) {
    this._students = this._validateArray(students, 'Students');
  }

  _validateString(value, propertyName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${propertyName} must be a string`);
    }
    return value;
  }

  _validateNumber(value, propertyName) {
    if (typeof value !== 'number') {
      throw new TypeError(`${propertyName} must be a number`);
    }
    return value;
  }

  _validateArray(value, propertyName) {
    if (!Array.isArray(value)) {
      throw new TypeError(`${propertyName} must be an array`);
    }
    return value;
  }
}
