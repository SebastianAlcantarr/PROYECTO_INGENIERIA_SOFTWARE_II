import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/tema1",
    component: () => import("../views/tema_1.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
