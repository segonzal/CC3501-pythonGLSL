#version 120
attribute vec3 position;
attribute vec4 color;
attribute vec3 normal;

varying vec4 myColor;
varying vec3 myNormal;
varying vec3 myPosition;

uniform vec3 lightPos;

void main(){
	myColor = color;
	myNormal = normal;
	myPosition = position;
	gl_Position = gl_ModelViewProjectionMatrix * vec4(myPosition,1.0);
}
