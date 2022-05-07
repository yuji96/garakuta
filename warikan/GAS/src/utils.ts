export function getEnv() {
  try {
    return PropertiesService.getScriptProperties().getProperty("ENV");
  } catch (ReferenceError) {
    return "LOCAL";
  }
}
