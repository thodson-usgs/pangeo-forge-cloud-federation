def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

BUCKET_PREFIX = "s3://<bucket-name>/<some-prefix>/"
# The storage backend we want
s3_fsspec = "s3fs.S3FileSystem"
# Credentials for the backend
s3_args = {
    "key": "<your-aws-access-key>",
    "secret": "<your-aws-access-secret>",
    "client_kwargs":{"region_name":"<your-aws-bucket-region>"}
}
# Take note: this is just python. We can reuse these values below
c.FlinkOperatorBakery.job_manager_resources = {"memory": "2048m", "cpu": 1.0}
c.FlinkOperatorBakery.task_manager_resources = {"memory": "2048m", "cpu": 1.0}
c.FlinkOperatorBakery.flink_configuration= {
   "taskmanager.numberOfTaskSlots": "1",
   "taskmanager.memory.flink.size": "1536m",
   "taskmanager.memory.task.off-heap.size": "256m",
   "taskmanager.memory.jvm-overhead.max": "1024m"
}
c.FlinkOperatorBakery.parallelism = 1
c.FlinkOperatorBakery.flink_version = "1.16"
# NOTE: image name must match the version of python and apache-beam being used locally
c.Bake.container_image = 'apache/beam_python3.9_sdk:2.50.0'
c.Bake.bakery_class = "pangeo_forge_runner.bakery.flink.FlinkOperatorBakery"

c.TargetStorage.fsspec_class = s3_fsspec
# Target output should be partitioned by `{{job_name}}`
c.TargetStorage.root_path = f"{BUCKET_PREFIX}/{{job_name}}/output"
c.TargetStorage.fsspec_args = s3_args

c.InputCacheStorage.fsspec_class = s3_fsspec
c.InputCacheStorage.fsspec_args = s3_args
# Input data cache should *not* be partitioned by `{{job_name}}`, as we want to get the datafile from the source only once
c.InputCacheStorage.root_path = f"{BUCKET_PREFIX}/cache/input"
