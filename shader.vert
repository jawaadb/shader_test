#version 330

#define PI (3.1415926)
#define FRAME_RATE (60)

in vec2 in_vert;
in vec3 in_color;

out vec3 v_color;

uniform int u_time;

const float amp = 0.05;
const float freq = 1;

void main() {
    v_color = in_color;

    float phase = in_vert.x * PI * 4;
    float offset_x = amp * cos(2 * PI * freq * u_time / FRAME_RATE + phase);
    float offset_y = amp * sin(2 * PI * freq * u_time / FRAME_RATE + phase);

    gl_Position = vec4(in_vert.x + offset_x, in_vert.y + offset_y, 0.0, 1.0);
}